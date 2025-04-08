import uuid
from django.db import models

from apps.core.utils import generate_incremental_code
from apps.users.models import User


class CompanyGroup(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code(CompanyGroup)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'companies'
        db_table = 'company_group'
        verbose_name = 'Grupo Empresarial'
        verbose_name_plural = 'Grupos Empresariais'


class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=10, unique=True)
    group = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE, related_name="companies")
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code(Company)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'companies'
        db_table = 'company'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Department(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code(Department)
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'companies'
        db_table = 'department'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.name


class AccessGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_permissions')
    company_set = models.ManyToManyField(Company, related_name="user_permissions")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'companies'
        db_table = 'access_group'
        verbose_name = 'Grupo de permissão'
        verbose_name_plural = 'Grupos de permissões'

    def __str__(self):
        return f"{self.user.username} @ permissions"

class AccessUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(AccessGroup, related_name="user_permissions")

    class Meta:
        app_label = 'companies'
        db_table = 'access_user'
        verbose_name = 'Permissão do usuário'
        verbose_name_plural = 'Permissões dos usuários'
