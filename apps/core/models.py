from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

User = get_user_model()


class CompanyGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    schema_name = models.CharField(max_length=50, unique=True)  # usado como schema do tenant
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    group = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE, related_name="companies")
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class UserCompanyPermission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="company_permissions")
    company = models.ForeignKey("core.Company", on_delete=models.CASCADE, related_name="user_permissions")
    can_view = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "company")
        verbose_name = "User Company Permission"
        verbose_name_plural = "User Company Permissions"

    def __str__(self):
        return f"{self.user.username} @ {self.company.name}"

