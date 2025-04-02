from django_tenants.middleware.main import TenantMainMiddleware
from django_tenants.utils import get_tenant_model
from django.core.exceptions import ImproperlyConfigured,DisallowedHost
from django.http.request import split_domain_port
from django.http import Http404
from django.db import connection
from apps.tenants.models import Domain


class TenantFromRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        try:
            domain, _ = split_domain_port(request.get_host())
        except DisallowedHost:
            raise ImproperlyConfigured("Domínio inválido. Verifique se está incluso no ALLOWED_HOSTS.")

        # Acesso por domínio (admin, frontend, etc)
        if domain and not request.path.startswith("/api/"):
            try:
                request.tenant = Domain.objects.select_related("tenant").get(domain=domain).tenant
            except Domain.DoesNotExist:
                raise ImproperlyConfigured(f"Tenant com domínio '{domain}' não encontrado.")
        # Acesso via API exige header
        else:
            tenant_header = request.headers.get("X-Tenant-ID")
            if not tenant_header:
                raise ImproperlyConfigured("X-Tenant-ID header is required for API access.")
            tenant_model = get_tenant_model()
            try:
                request.tenant = tenant_model.objects.get(schema_name=tenant_header)
            except tenant_model.DoesNotExist:
                raise ImproperlyConfigured(f"Tenant com schema '{tenant_header}' não encontrado.")


# class TenantFromHeaderMiddleware(TenantMainMiddleware):
#     def __init__(self, get_response):
#         super().__init__(get_response)
#         self.get_response = get_response
#
#     def process_request(self, request):
#         # Ignora validação para o admin ou schema público
#         if request.path.startswith("/admin"):
#             return
#
#         tenant_id = request.headers.get("X-Tenant-ID")
#         if not tenant_id:
#             raise ImproperlyConfigured("X-Tenant-ID header is required.")
#
#         tenant_model = get_tenant_model()
#
#         try:
#             tenant = tenant_model.objects.get(schema_name=tenant_id)
#         except tenant_model.DoesNotExist:
#             raise Http404("Tenant not found.")
#
#         request.tenant = tenant
#         connection.set_schema(schema_name=tenant.schema_name)
