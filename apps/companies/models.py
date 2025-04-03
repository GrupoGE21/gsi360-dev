from django.db import models
from apps.users.models import CustomUser


class CompanyGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        app_label = 'companies'


class Company(models.Model):
    group = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE, related_name="companies")
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        app_label = 'companies'


class UserCompanyPermission(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrator'),
        ('MANAGER', 'Manager'),
        ('EMPLOYEE', 'Employee'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='company_permissions')
    company_set = models.ManyToManyField(Company, related_name="user_permissions")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'companies'

    def __str__(self):
        return f"{self.user.username} @ permissions"
