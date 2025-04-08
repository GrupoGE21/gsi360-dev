from django.contrib import admin
from .models import Company, CompanyGroup, Department


@admin.register(CompanyGroup)
class CompanyGroupAdmin(admin.ModelAdmin):
    readonly_fields = ("code",)
    list_display = ("code", "name", "created_at", "updated_at")
    list_display_links = ("code", "name",)
    search_fields = ("name",)
    ordering = ("-code",)
    list_per_page = 50

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ("code",)
    list_display = ("code", "name", "created_at", "updated_at")
    list_display_links = ("code", "name",)
    search_fields = ("name",)
    ordering = ("-code",)
    list_per_page = 50


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ("code",)
    list_display = ("code", "name", "created_at", "updated_at")
    list_display_links = ("code", "name",)
    search_fields = ("name",)
    ordering = ("-code",)
    list_per_page = 50
