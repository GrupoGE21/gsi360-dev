from django.contrib import admin
from .models import Company, CompanyGroup, AccessGroup, AccessUser

@admin.register(CompanyGroup)
class CompanyGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 50

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 50


@admin.register(AccessGroup)
class AccessGroupAdmin(admin.ModelAdmin):
    # list_display = ("id", "user", "role")
    # list_display_links = ("id", "user", "role")
    # list_filter = ("role",)
    list_per_page = 50


@admin.register(AccessUser)
class AccessUserAdmin(admin.ModelAdmin):
    # list_display = ("id", "user", "role")
    # list_display_links = ("id", "user", "role")
    # list_filter = ("role",)
    list_per_page = 50
