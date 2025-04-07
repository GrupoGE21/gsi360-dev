from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email_professional", "registration_date_at", "update_date_at")
    list_display_links = ("full_name",)
    search_fields = ("first_name",)
    list_per_page = 50
