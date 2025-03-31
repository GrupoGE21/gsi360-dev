from django_tenants.middleware.main import TenantMainMiddleware
from django_tenants.utils import get_tenant_model
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.db import connection


class TenantFromHeaderMiddleware(TenantMainMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response

    def process_request(self, request):
        # ✅ Ignora validação para o admin ou schema público
        if request.path.startswith("/admin"):
            return

        tenant_id = request.headers.get("X-Tenant-ID")
        if not tenant_id:
            raise ImproperlyConfigured("X-Tenant-ID header is required.")

        tenantModel = get_tenant_model()

        try:
            tenant = tenantModel.objects.get(schema_name=tenant_id)
        except tenantModel.DoesNotExist:
            raise Http404("Tenant not found.")

        request.tenant = tenant
        connection.set_schema(schema_name=tenant.schema_name)
