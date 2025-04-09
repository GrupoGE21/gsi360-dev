from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    readonly_fields = ('code', 'registration_date_at', 'update_date_at')
    ordering = ('code',)
    list_display = ('code', 'first_name', 'last_name', 'email_professional', 'is_active')

    fieldsets = (
        ("Identificação", {
            'fields': ('code', 'first_name', 'last_name', 'sex', 'birth_date', 'cpf', 'doc_identity', 'number_pis', 'cnpj', 'marital_status')
        }),
        ("Contato", {
            'fields': ('email_professional', 'email_personal', 'phone_number', 'phone_number_company')
        }),
        ("Endereço", {
            'fields': ('cep', 'address', 'address_number', 'address_complement', 'neighborhood', 'city')
        }),
        ("Informações Profissionais", {
            'fields': ('job_title', 'hierarchy_level', 'admission_date', 'leader', 'work_schedule_type', 'employment_type', 'academic_background', 'resignation_date')
        }),
        ("Recursos Humanos", {
            'fields': ('uses_timesheet', 'has_time_bank', 'has_vacation', 'spouse_or_children', 'additional_info')
        }),
        ("Permissões", {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ("Auditoria", {
            'fields': ('registration_date_at', 'update_date_at')
        }),
    )
    list_per_page = 50
