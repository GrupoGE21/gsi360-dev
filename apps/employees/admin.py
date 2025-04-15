from django.contrib import admin
from .models import EmployeeCost, Employee, Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("full_name", "created_at")
    list_filter = ("full_name",)
    search_fields = ("full_name",)
    ordering = ("full_name",)
    list_per_page = 50


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("code", "full_name", "created_at", "updated_at")
    list_display_links = ("code", "full_name",)
    search_fields = ("first_name", "code")
    ordering = ("-code",)
    list_per_page = 50


@admin.register(EmployeeCost)
class EmployeeCostAdmin(admin.ModelAdmin):
    list_display = ("id", "cost_type", "created_at", "updated_at")
    list_display_links = ("id", "cost_type",)
    search_fields = ("cost_type",)
    ordering = ("-id",)
    list_per_page = 50
