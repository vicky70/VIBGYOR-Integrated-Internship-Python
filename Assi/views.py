from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from .serializers import DepartmentSerializer
from .models import DepartmentModel


# ()    @
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getDepartmentList(request):
    departmentList = DepartmentModel.objects.filter(status=True)
    return Response({'DepartmentList': DepartmentSerializer(departmentList, many=True).data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateDepartment(request, id):
    try:
        department = DepartmentModel.objects.get(pk=id)
        serializer = DepartmentSerializer(instance=department, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Department updated successfully.'}, 
                status=status.HTTP_202_ACCEPTED
            )
        return Response({'error': 'Invalid data please provide proper data'}, status=status.HTTP_204_NO_CONTENT)
    except DepartmentModel.DoesNotExist:
        return Response({'error': 'Department Does not exists.'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteDeparment(request, id):
    try:
        department = DepartmentModel.objects.get(pk=id)
        if not department.status:
            return Response({'error': 'Department already Deleted'}, status=status.HTTP_400_BAD_REQUEST)
        department.status = False
        department.save()
        return Response({'message': 'Department deleted Successfully'}, status=status.HTTP_200_OK)
    except DepartmentModel.DoesNotExist:
        return Response({'error': "Department Does not exists"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDepartment(request):
    serializer = DepartmentSerializer(data=request.data)

    if serializer.is_valid():
        department = serializer.save()
        return Response({'Department': DepartmentSerializer(department).data, 
                        'message': 'New Department created successfully.'}, 
                        status=status.HTTP_201_CREATED)
    
    return Response({
        'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Please Provide username or password both'}, status=status.HTTP_401_UNAUTHORIZED)
    
    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': user.username}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credientials'}, status=status.HTTP_401_UNAUTHORIZED)

