from django.db import models

class EmployeeCost(models.Model):
    name = models.CharField('Tipo de custo', max_length=100)
    description = models.TextField(verbose_name='Descrição')
    is_active = models.BooleanField('Está ativo?', default=True)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='employee_costs_created')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='employee_costs_updated')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Custo do profissional'
        verbose_name_plural = 'Custos dos profissionais'