import uuid
from django.db import models
from apps.core.utils import generate_incremental_code

# TODO: verificar campos
class Client(models.Model):
    PERSON_TYPE_CHOICES = (
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField('Código', max_length=10, unique=True)
    name = models.CharField('Nome', max_length=100)
    client_acronym = models.CharField('Sigla da empresa', max_length=20)
    group_company = models.CharField('Grupo empresarial', max_length=100, blank=True, null=True)
    person_type = models.CharField('Tipo de pessoa', max_length=1, choices=PERSON_TYPE_CHOICES)
    geographic_market = models.CharField('Mercado geográfico', max_length=100, blank=True, null=True)
    vertical_market = models.CharField('Mercado vertical', max_length=100, blank=True, null=True)
    phone_number = models.CharField('Telefone', max_length=20, blank=True, null=True)
    site = models.CharField('Site', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField('Data de cadastro', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='clients_created')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='clients_updated')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code(Client)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'clients'
        db_table = 'clients'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

# TODO: verificar campos
class ClientCNPJ(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField('Código', max_length=10, unique=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name="clients_cnpj")
    cnpj = models.CharField('CNPJ', max_length=14, unique=True)
    legal_name = models.CharField('Razão social', max_length=100, blank=True, null=True)
    state_registration = models.CharField('Inscrição estadual', max_length=100, blank=True, null=True)
    municipal_registration = models.CharField('Inscrição municipal', max_length=250, blank=True, null=True)
    address = models.CharField('Rua', max_length=100, blank=True, null=True)
    address_number = models.CharField('Número', max_length=20, blank=True, null=True)
    complement = models.CharField('Complemento', max_length=100, blank=True, null=True)
    neighborhood = models.CharField('Bairro', max_length=100, blank=True, null=True)
    cep = models.CharField('CEP', max_length=8, blank=True, null=True)
    city = models.CharField('Cidade', max_length=100, blank=True, null=True)
    state = models.CharField('Estado', max_length=100, blank=True, null=True)
    email = models.CharField('Email', max_length=250, blank=True, null=True)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    created_at = models.DateTimeField('Data de cadastro', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='clients_cnpj_created')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='clients_cnpj_updated')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code(ClientCNPJ)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.cnpj

    class Meta:
        app_label = 'clients'
        db_table = 'clients_cnpj'
        verbose_name = 'Cliente CNPJ'
        verbose_name_plural = 'Clientes CNPJ'

# TODO: verificar campos
class ClientProfessional(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField('Código', max_length=10, unique=True)
    name = models.CharField('Nome', max_length=100)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name="clients_professionals")
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    cellphone = models.CharField('Celular', max_length=20, blank=True, null=True)
    email = models.CharField('Email', max_length=250, blank=True, null=True)
    position = models.CharField('Cargo', max_length=100, blank=True, null=True)
    sector = models.CharField('Setor', max_length=100, blank=True, null=True)
    created_at = models.DateTimeField('Data de cadastro', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='clients_professional_created')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='clients_professional_updated')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code(ClientProfessional)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'clients'
        db_table = 'clients_professional'
        verbose_name = 'Profissional do Cliente'
        verbose_name_plural = 'Profissionais dos Clientes'
