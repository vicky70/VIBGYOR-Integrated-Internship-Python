from django.urls import path
from . import views

urlpatterns = [
    path('createDeparment/', views.createDepartment, name='createDepartment'),
    path('getDepartmentList/', views.getDepartmentList, name='getDepartmentList'),
    path('updateDepartment/<int:id>/', views.updateDepartment, name='updateDepartment'),
    path('deleteDepartment/<int:id>/', views.deleteDeparment, name='deleteDepartment'),
    path('adminlogin/', views.login, name='adminlogin'),
]