from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=90, null=False, blank=False, verbose_name='ФИО')
    phone = models.CharField(max_length=16, blank=False, verbose_name='Телефон',)
    address = models.CharField(max_length=200, verbose_name='Адрес', blank=False)

