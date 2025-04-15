from django.contrib import admin
from .models import PartnerCompany

@admin.register(PartnerCompany)
class PartnerCompanyAdmin(admin.ModelAdmin):
    list_display = ("code", "legal_name", "created_at", "updated_at")
    list_display_links = ("code", "legal_name",)
    search_fields = ("legal_name", "code")
    ordering = ("-code",)
    list_per_page = 50
