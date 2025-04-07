import uuid
from django.db import models
from apps.users.models import User


class CompanyGroup(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'companies'
        db_table = 'company_group'


class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE, related_name="companies")
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        app_label = 'companies'
        db_table = 'company'


class Department(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'companies'
        db_table = 'department'



class AccessGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_permissions')
    company_set = models.ManyToManyField(Company, related_name="user_permissions")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'companies'
        db_table = 'access_group'

    def __str__(self):
        return f"{self.user.username} @ permissions"

class AccessUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(AccessGroup, related_name="user_permissions")

    class Meta:
        app_label = 'companies'
        db_table = 'access_user'
