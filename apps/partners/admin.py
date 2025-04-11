from django.contrib import admin
from .models import PartnerCompany

@admin.register(PartnerCompany)
class PartnerCompanyAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "created_at", "updated_at")
    list_display_links = ("code", "name",)
    search_fields = ("name",)
    ordering = ("-code",)
    list_per_page = 50
