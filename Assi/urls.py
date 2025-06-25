from django.urls import path
from . import views

urlpatterns = [
    path('createDepartment/', views.createDepartment, name='createDepartment'),
    path('getDepartmentList/', views.getDepartmentList, name='getDepartmentList'),
    path('updateDepartment/<int:id>/', views.updateDepartment, name='updateDepartment'),
    path('deleteDepartment/<int:id>/', views.deleteDeparment, name='deleteDepartment'),

    path('createRole/', views.createRole, name="createRole"),
    path('getRoleList/', views.getRolesList, name="roleList"),
    path('updateRole/<int:id>/', views.updateRole, name="updateRole"),
    path('deleteRole/<int:id>/', views.deleteRole, name="deleteRole"),

    path('adminlogin/', views.login, name='adminlogin'),
]