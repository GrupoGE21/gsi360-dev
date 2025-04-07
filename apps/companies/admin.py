from django.contrib import admin
from .models import Company, CompanyGroup, UserCompanyPermission

@admin.register(CompanyGroup)
class CompanyGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_display_links = ("id","name",)
    search_fields = ("name",)
    list_per_page = 50

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_display_links = ("id", "name",)
    search_fields = ("name",)
    list_per_page = 50


@admin.register(UserCompanyPermission)
class UserCompanyPermissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "role")
    list_display_links = ("id", "user", "role")
    list_filter = ("role",)
    list_per_page = 50
