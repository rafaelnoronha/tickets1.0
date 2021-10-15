from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    numero_tentativas_login = models.PositiveSmallIntegerField(
        verbose_name='Número de tentativas falhas de login',
        default=0,
    )

    verificacao_duas_etapas = models.BooleanField(
        verbose_name='Verificação em duas etapas',
        default=False,
    )
