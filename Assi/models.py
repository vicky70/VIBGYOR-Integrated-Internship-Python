from django.db import models

#  ()  

class DepartmentModel(models.Model):
    dept_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.dept_name

class RolesModel(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Team Leader', 'Team Leader'),
        ('Employee', 'Employee'),
    ]
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, choices=ROLE_CHOICES)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.role_name