from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    numero_tentativas_login = models.PositiveSmallIntegerField(
        verbose_name='Número de tentativas falhas de login',
        default=0,
    )

    verificacao_em_duas_etapas = models.BooleanField(
        verbose_name='Verificação em duas etapas',
        default=False,
    )

    codigo_verificacao_segunda_etapa = models.CharField(
        verbose_name='Código de verificação da segunda etapa',
        max_length=4,
    )
