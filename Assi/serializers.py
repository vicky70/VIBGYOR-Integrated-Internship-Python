from rest_framework import serializers
from .models import DepartmentModel, RolesModel

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = ['id', 'dept_name', 'description', 'created_at', 'updated_at', 'status']

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesModel
        fields = ['role_id', 'role_name', 'description', 'created_at', 'updated_at', 'status']

