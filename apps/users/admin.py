from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("code",)
    list_display = ("code", "full_name", "email_professional", "registration_date_at", "update_date_at")
    list_display_links = ("code", "full_name",)
    search_fields = ("first_name",)
    ordering = ("-code",)
    list_per_page = 50
