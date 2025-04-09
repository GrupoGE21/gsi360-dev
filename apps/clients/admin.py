from django.contrib import admin
from .models import Client, ClientCNPJ, ClientProfessional


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ("code",)
    list_display = ("code", "name", "created_at", "updated_at")
    list_display_links = ("code", "name",)
    search_fields = ("name",)
    ordering = ("-code",)
    list_per_page = 50


@admin.register(ClientCNPJ)
class ClientCNPJAdmin(admin.ModelAdmin):
    readonly_fields = ("code",)
    list_display = ("code", "cnpj", "created_at", "updated_at")
    list_display_links = ("code", "cnpj",)
    search_fields = ("cnpj",)
    ordering = ("-code",)
    list_per_page = 50


@admin.register(ClientProfessional)
class ClientProfessionalAdmin(admin.ModelAdmin):
    readonly_fields = ("code",)
    list_display = ("code", "name", "created_at", "updated_at")
    list_display_links = ("code", "name",)
    search_fields = ("name",)
    ordering = ("-code",)
    list_per_page = 50