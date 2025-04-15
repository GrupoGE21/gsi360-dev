import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.db import models
from django.utils import timezone
from apps.core.utils import generate_incremental_code
from apps.users.managers import UserManager

# TODO: remover os campos
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField('Nome', max_length=255, blank=True)
    last_name = models.CharField('Sobrenome', max_length=255, blank=True)
    permissions_groups = models.ManyToManyField(Group, blank=True, verbose_name="Grupos de permissões", related_name='user_permissions')
    email_professional = models.EmailField('E-mail da empresa',max_length=255, unique=True)
    is_staff = models.BooleanField('Pode acessar o admin?', default=True)
    is_superuser = models.BooleanField('É super usuário?', default=False)
    created_at = models.DateTimeField('Usuário criado em', default=timezone.now)
    update_date_at = models.DateTimeField('Usuário Atualizado em', auto_now=True)

    USERNAME_FIELD = 'email_professional'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email_professional

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "-"

    class Meta:
        app_label = 'users'
        db_table = 'user'
        verbose_name = 'Usuário'
