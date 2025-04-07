from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email_professional, password=None, **extra_fields):
        if not email_professional:
            raise ValueError('O e-mail profissional é obrigatório')
        email_professional = self.normalize_email(email_professional)
        user = self.model(email_professional=email_professional, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_professional, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa de is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa de is_superuser=True.')

        return self.create_user(email_professional, password, **extra_fields)
