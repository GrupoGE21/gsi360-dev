import uuid
from django.db import models
from ..core.utils import generate_incremental_code

# TODO: verificar campos
class PartnerCompany(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField('Código da empresa', max_length=10, unique=True)
    legal_name = models.CharField('Nome', max_length=250)
    cnpj = models.CharField('CNPJ', max_length=14, unique=True)
    description = models.TextField('Descrição', blank=True, null=True)
    is_active = models.BooleanField('Está ativo?', default=True)
    created_at = models.DateTimeField('Data de cadastro', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code(PartnerCompany, digits=6)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.legal_name

    class Meta:
        app_label = 'partners'
        db_table = 'partner_company'
        ordering = ['-created_at']
        verbose_name = 'Empresa parceira'
        verbose_name_plural = 'Empresas parceiras'

