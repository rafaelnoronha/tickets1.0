from django.db import models
from usuarios.models import Usuario
import uuid


class Base(models.Model):
    uuid = models.UUIDField(
        verbose_name='UUID',
        default=uuid.uuid4(),
    )

    ativo = models.BooleanField(
        verbose_name='Ativo',
        default=True,
    )

    data_cadastro = models.DateField(
        verbose_name='Data do cadastro',
        auto_now_add=True,
    )

    hora_cadastro = models.TimeField(
        verbose_name='Hora do cadastro',
        auto_now_add=True,
    )

    usuario_cadastro = models.ForeignKey(
        Usuario,
        verbose_name='Usuário que efetuou o cadastro',
        on_delete=models.PROTECT,
        related_name='usuario_cadastro_data',
    )

    class Meta:
        abstract = True
