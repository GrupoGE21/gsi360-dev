import uuid
from django.db import models


class Opportunity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField('Código', max_length=20, unique=True)
    name = models.CharField('Nome', max_length=100)
    num_code = models.CharField('Número do código', max_length=20)
    client = models.ForeignKey('clients.Client', on_delete=models.SET_NULL, max_length=20, blank=True, null=True)
    opportunity_value = models.FloatField('Valor da Oportunidade', blank=True, null=True)
    status = models.CharField('Status', max_length=20)
    status_reason = models.CharField('Razão do Status', max_length=20)
    initial_date_op = models.DateTimeField('Data de inicio da proposta', blank=True, null=True)
    initial_date_proj = models.DateTimeField('Data de inicio do projeto', blank=True, null=True)
    end_date = models.DateTimeField('Data final da Oportunidade', blank=True, null=True)
    is_approved = models.BooleanField('Está aprovado?', default=False)
    name_folder = models.CharField('Nome da pasta', max_length=100)
    activities = models.TextField('Atividades', blank=True, null=True)
    obs = models.TextField('Observações', blank=True, null=True)
    characteristics = models.TextField('Características', blank=True, null=True)
    objectivity = models.TextField('Objetivos', blank=True, null=True)
    created_at = models.DateTimeField('Data de cadastro', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='created_by')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='updated_by')

