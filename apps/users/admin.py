from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    readonly_fields = ('created_at', 'update_date_at')
    ordering = ('-created_at',)
    list_display = ('full_name', 'email_professional')
    list_per_page = 50
