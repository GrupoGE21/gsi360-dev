from django_tenants.utils import schema_context, get_tenant_model
from django.contrib.auth import get_user_model

User = get_user_model()
TenantModel = get_tenant_model()

admin_username = "admin"
admin_password = "admin"

for tenant in TenantModel.objects.all():
    schema = tenant.schema_name
    print(f"\n🔍 Verificando schema: {schema}")

    with schema_context(schema):
        if User.objects.filter(username=admin_username).exists():
            print(f"✅ Usuário '{admin_username}' já existe no schema '{schema}'")
        else:
            print(f"⚠️ Usuário '{admin_username}' NÃO existe em '{schema}' — criando...")
            User.objects.create_superuser(username=admin_username, password=admin_password)
            print(f"✅ Criado com sucesso!")
