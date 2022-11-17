from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Company


class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=254
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='employees',
        null=True
    )
    REQUIRED_FIELDS = ['email', 'first_name',
                       'last_name', 'password']

    def __str__(self):
        return self.username
