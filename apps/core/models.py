from django.db import models

# Tipo de contratação do profissional - ex.: pj, clt, estágio etc
class EmploymentType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Tipos de custos dos profissionais
class EmployeeCostType(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField('Está ativo?', default=True)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)

    def __str__(self):
        return self.name
