from django.db import models

# Tipo de contratação do profissional - ex.: pj, clt, estágio etc
class EmploymentType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'
        db_table = 'employment_type'
        verbose_name = "Tipo de contratação"
        verbose_name_plural = "Tipos de contratação"


# Tipos de custos dos profissionais
class EmployeeCostType(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField('Está ativo?', default=True)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'
        db_table = 'employee_cost_type'
        verbose_name = 'Tipo de custo do profissional'
        verbose_name_plural = 'Tipos de custos do profissional'


# cadcliente - cliente
# cadclientecnpj
# cadagente - profissionais do cliente