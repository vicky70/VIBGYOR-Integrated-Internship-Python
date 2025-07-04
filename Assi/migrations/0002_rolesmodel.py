# Generated by Django 5.2.3 on 2025-06-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolesModel',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Team Leader', 'Team Leader'), ('Employee', 'Employee')], max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
