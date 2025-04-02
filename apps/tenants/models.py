from django.db import models
# from django_tenants.models import TenantMixin, DomainMixin

# class TenantCompany(TenantMixin):
#     name = models.CharField(max_length=255)
#     created_on = models.DateField(auto_now_add=True)
#     paid_until = models.DateField(null=True, blank=True)
#     on_trial = models.BooleanField(default=True)
#
#     auto_create_schema = True
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         app_label = 'tenants'
#
# class Domain(DomainMixin):
#     tenant = models.ForeignKey(TenantCompany, on_delete=models.CASCADE, related_name='domains')
#
#     class Meta:
#         app_label = 'tenants'