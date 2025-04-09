from django.contrib import admin
from .models import EmployeeCost


@admin.register(EmployeeCost)
class EmployeeCostAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_display_links = ("id", "name",)
    search_fields = ("name",)
    ordering = ("-id",)
    list_per_page = 50