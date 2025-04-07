import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models
from apps.users.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email_professional = models.EmailField('E-mail da empresa',max_length=255, unique=True)
    email_personal = models.EmailField('E-mail pessoal',max_length=255, unique=True)
    birth_date = models.DateField('Data de nascimento', null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11)
    cnpj = models.CharField('CNPJ', max_length=14, blank=True, null=True)
    doc_identity = models.CharField('Documento de identidade', max_length=10, blank=True, null=True)
    number_pis = models.CharField('Número do PIS', max_length=20, blank=True, null=True)
    marital_status = models.CharField('Estado civil', max_length=20, blank=True, null=True)
    phone_number = models.CharField('Celular pessoal', max_length=20)
    phone_number_company = models.CharField('Celular da empresa', max_length=20, blank=True, null=True)
    cep = models.CharField('CEP', max_length=20)
    address = models.CharField(max_length=255, blank=True, null=True)
    address_number = models.CharField('Número da casa/apto', max_length=10, blank=True, null=True)
    address_complement = models.CharField('Complemento endereço', max_length=20, blank=True, null=True)
    neighborhood = models.CharField('Bairro', max_length=20, blank=True, null=True)
    city = models.CharField('Cidade', max_length=50, blank=True, null=True)
    admission_date = models.DateField('Data de admissão', blank=True, null=True)
    is_clt = models.BooleanField('É CLT?', default=False)
    is_pj = models.BooleanField('É PJ?', default=False)
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
    registration_date_at = models.DateTimeField('Usuário Registrado em', auto_now_add=True)
    update_date_at = models.DateTimeField('Usuário Atualizado em', auto_now=True)

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "-"

    USERNAME_FIELD = 'email_professional'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    objects = UserManager()

    class Meta:
        db_table = 'user'