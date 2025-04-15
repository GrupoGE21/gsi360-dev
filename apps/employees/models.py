from django.db import models
import uuid

from apps.companies.models import Company, Department
from apps.core.utils import generate_incremental_code
from apps.users.models import User

# TODO: verificar campos
class Candidate(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Empresa')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Departamento')
    full_name = models.CharField('Nome completo', max_length=200)
    phone_number = models.CharField('Celular', max_length=20)
    email = models.EmailField('Email', max_length=250)
    created_at = models.DateTimeField('Data de cadastro', auto_now_add=True)
    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cadastrado por", related_name="requested_candidates")
    is_approved = models.BooleanField('Foi aprovado?', default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Aprovado por", related_name="approved_candidates")
    approved_at = models.DateField('Data de aprovação', auto_now=True, null=True, blank=True)
    job_title = models.CharField('Cargo ou função', max_length=250, blank=True, null=True)
    hiring_reason = models.CharField('Motivo da contratação', max_length=200, null=True, blank=True)
    work_description = models.TextField('Escopo de trabalho', null=True, blank=True)
    is_overhead = models.BooleanField('É overhead?', default=False)
    is_in_budget = models.BooleanField('Está dentro do orçamento?', default=False)
    employment_type = models.ForeignKey('core.EmploymentType', on_delete=models.SET_NULL, max_length=20, blank=True, null=True, verbose_name='Tipo de contratação')
    work_schedule_type = models.CharField('Regime de trabalho', max_length=20, blank=True, null=True)
    work_location = models.CharField('Local de trabalho', max_length=100, blank=True, null=True)
    start_date = models.DateField('Data de inicio', null=True, blank=True)
    end_date = models.DateField('Data de fim', null=True, blank=True)
    needs_badge = models.BooleanField('Precisa de crachá?', default=True)
    has_health_ensurance = models.BooleanField('Tem plano de saúde?', default=True)
    has_dental_ensurance = models.BooleanField('Tem plano de odontológico?', default=True)
    has_life_ensurance = models.BooleanField('Tem seguro de vida?', default=True)
    has_ticket = models.BooleanField('Tem ticket?', default=True)
    ticket_value = models.FloatField('Valor do ticket', default=0.0)
    has_transport_ticket = models.BooleanField('Tem vale transporte?', default=True)
    needs_laptop = models.BooleanField('Precisa de computador?', default=True)
    needs_uniform = models.BooleanField('Precisa de uniforme?', default=False)
    shirt_size = models.CharField('Tamanho da camisa', max_length=10, blank=True, null=True)
    pants_size = models.CharField('Tamanho da calça', max_length=10, blank=True, null=True)
    shoes_size = models.CharField('Tamanho do sapato', max_length=10, blank=True, null=True)
    will_conduct_vehicle = models.BooleanField('Vai conduzir um veículo?', default=True)
    is_user = models.BooleanField('Terá acesso ao GSI360?', default=True)
    notes = models.TextField(blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Última atualização feito por")
    updated_at = models.DateTimeField('Última atualização', auto_now=True)


    def __str__(self):
        return self.full_name

    class Meta:
        app_label = 'employees'
        db_table = 'candidate'
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ['-created_at']

# TODO: verificar campos
class Employee(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField('Matrícula', max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    email_personal = models.EmailField('E-mail pessoal', max_length=255, blank=True, null=True)
    birth_date = models.DateField('Data de nascimento', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11)
    cnpj = models.CharField('CNPJ', max_length=14, blank=True, null=True)
    doc_identity = models.CharField('Documento de identidade', max_length=10, blank=True, null=True, unique=True)
    number_pis = models.CharField('Número do PIS', max_length=20, blank=True, null=True, unique=True)
    marital_status = models.CharField('Estado civil', max_length=20, blank=True, null=True)
    phone_number = models.CharField('Celular pessoal', max_length=20)
    phone_number_company = models.CharField('Celular da empresa', max_length=20, blank=True, null=True)
    cep = models.CharField('CEP', max_length=20)
    address = models.CharField('Rua', max_length=255, blank=True, null=True)
    address_number = models.CharField('Número da casa/apto', max_length=10, blank=True, null=True)
    address_complement = models.CharField('Complemento endereço', max_length=20, blank=True, null=True)
    neighborhood = models.CharField('Bairro', max_length=20, blank=True, null=True)
    city = models.CharField('Cidade', max_length=50, blank=True, null=True)
    admission_date = models.DateField('Data de admissão', blank=True, null=True)
    work_schedule_type = models.CharField('Regime de trabalho', max_length=20, blank=True, null=True)
    resignation_date = models.DateField('Data de demissão', blank=True, null=True)
    academic_background = models.CharField('Formação acadêmica', max_length=100, blank=True, null=True)
    job_title = models.CharField('Cargo', max_length=100, blank=True, null=True)
    hierarchy_level = models.CharField('Hierarquia', max_length=50, blank=True, null=True)
    sex = models.CharField('Sexo', max_length=20, blank=True, null=True)
    is_active = models.BooleanField('Está ativo?', default=True)
    uses_timesheet = models.BooleanField('Faz TimeSheet?', default=True)
    has_time_bank = models.BooleanField('Tem banco de horas?', default=True)
    spouse_or_children = models.CharField('Cônjuge e/ou filhos', max_length=250, blank=True, null=True)
    additional_info = models.CharField('Informações adicionais', max_length=250, blank=True, null=True)
    has_vacation = models.BooleanField('Tem férias?', default=True)
    leader = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Líder", related_name='team_members')
    employment_type = models.ForeignKey('core.EmploymentType', on_delete=models.SET_NULL, max_length=20, blank=True, null=True, verbose_name='Tipo de contratação', related_name='employees')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_incremental_code(Employee, digits=6)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def __str__(self):
        return self.full_name

    class Meta:
        app_label = 'employees'
        db_table = 'employee'
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering = ['-created_at']

# TODO: verificar campos
class EmployeeCost(models.Model):
    cost_type = models.ForeignKey('core.EmployeeCostType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tipo de custo')
    description = models.TextField(verbose_name='Descrição')
    is_active = models.BooleanField('Está ativo?', default=True)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Última atualização', auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='employee_costs_created')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, related_name='employee_costs_updated')

    def __str__(self):
        return self.cost_type

    class Meta:
        app_label = 'employees'
        db_table = 'employee_cost'
        verbose_name = 'Custo do profissional'
        verbose_name_plural = 'Custos dos profissionais'
