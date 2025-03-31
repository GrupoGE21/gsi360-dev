from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    cognito_sub = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.username
