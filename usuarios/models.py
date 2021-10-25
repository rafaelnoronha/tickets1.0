from django.db import models
from django.contrib.auth.models import AbstractUser
from empresas.models import Empresa
import uuid


class Usuario(AbstractUser):
    uuid = models.UUIDField(
        verbose_name='UUID',
        default=uuid.uuid4()
    )

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
    )

    celular = models.CharField(
        verbose_name='Celular',
        max_length=11,
        default='',
    )

    media_avaliacoes = models.DecimalField(
        verbose_name='Média das avaliações',
        max_digits=2,
        decimal_places=1,
        default=0,
    )

    empresa = models.ForeignKey(
        Empresa,
        verbose_name='Empresa',
        related_name='empresa',
        on_delete=models.PROTECT,
    )

    observacoes = models.TextField(
        verbose_name='Observações',
    )

    numero_tentativas_login = models.PositiveSmallIntegerField(
        verbose_name='Número de tentativas falhas de login',
        default=0,
    )

    verificacao_duas_etapas = models.BooleanField(
        verbose_name='Verificação em duas etapas',
        default=False,
    )

    codigo_verificacao_segunda_etapa = models.CharField(
        verbose_name='Código de verificação da segunda etapa',
        max_length=4,
    )

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name} [{self.username}]'


class log_autenticacao(models.model):
    uuid = models.UUIDField(
        verbose_name='UUID',
        default=uuid.uuid4(),
    )

    ip = models.IPAddressField(
        verbose_name='IP',
    )

    usuario = models.ForeignKey(
        Usuario,
        verbose_name='Usuário',
        related_name='usuario',
        on_delete=models.PROTECT,
    )

    autenticado = models.BooleanField(
        verbose_name='Autenticado',
        default=False,
    )

    data_autenticacao = models.DateField(
        verbose_name='Data da autenticação',
        auto_now_add=True,
    )

    hora_autenticacao = models.TimeField(
        verbose_name='Hora da autenticação',
        auto_now_add=True,
    )

    class Meta:
        db_table = 'log_autenticacao'
        verbose_name = 'Log de autenticação'
        verbose_name_plural = 'Logs de autenticação'

    def __str__(self):
        return f'{self.id} - {self.usuario} [{self.autenticado}]'
