from django.db import models
from django.contrib.auth.models import AbstractUser
from empresa.models import Empresa
import uuid


class Usuario(AbstractUser):
    """
    Modelo de usuários do sistema, tanto dos usuários que vão abrir, quanto aos que vão solucionar os tickets. No caso
    dos usuários que vão soluciuonar os tickets, eles não vão ter nenhuma empresa vinculada a eles.
    """

    uuid = models.UUIDField(
        verbose_name='UUID',
        default=uuid.uuid4(),
        help_text='UUID Código único não sequencial',
    )

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        help_text='Telefone fixo ex: 3100000000',
    )

    celular = models.CharField(
        verbose_name='Celular',
        max_length=11,
        default='',
        blank=True,
        help_text='Telefone celular ex: 31900000000',
    )

    media_avaliacoes = models.DecimalField(
        verbose_name='Média das avaliações',
        max_digits=2,
        decimal_places=1,
        default=0,
        help_text='Média das avaliações dos chamados avaliados',
    )

    empresa = models.ForeignKey(
        Empresa,
        verbose_name='Empresa',
        related_name='empresa_empresa_usuario',
        on_delete=models.PROTECT,
        help_text='Empresa a qual o usuário pertence',
    )

    observacoes = models.TextField(
        verbose_name='Observações',
        default='',
        blank=True,
        help_text='Observações referênte ao usuário',
    )

    numero_tentativas_login = models.PositiveSmallIntegerField(
        verbose_name='Número de tentativas falhas de login',
        default=0,
        help_text='Número de tentativas falhas ao fazer login',
    )

    verificacao_duas_etapas = models.BooleanField(
        verbose_name='Verificação em duas etapas',
        default=False,
        help_text='Se deve exigir ou não a verificação da segunda etapa no login',
    )

    codigo_verificacao_segunda_etapa = models.CharField(
        verbose_name='Código de verificação da segunda etapa',
        max_length=4,
        help_text='O código que valida a verificação da segunda etapa, como a senha ao fazer o login',
    )

    data_cadastro = models.DateField(
        verbose_name='Data do cadastro',
        auto_now_add=True,
        help_text='Data do cadastro do usuário',
    )

    hora_cadastro = models.TimeField(
        verbose_name='Hora do cadastro',
        auto_now_add=True,
        help_text='Hora do cadastro do usuário',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name} [{self.username}]'


class LogAutenticacao(models.Model):
    """
    Modelo que vai guardar as tentativas de login, tanto as que tiveram sucesso quanto as que falharem.
    """

    uuid = models.UUIDField(
        verbose_name='UUID',
        default=uuid.uuid4(),
        help_text='UUID Código único não sequencial',
    )

    ip = models.GenericIPAddressField(
        verbose_name='IP',
        help_text='Endereço IP do cliente/dispositivo',
    )

    usuario = models.ForeignKey(
        Usuario,
        verbose_name='Usuário',
        related_name='usuario_usuario_log_autenticacao',
        on_delete=models.PROTECT,
        help_text='Usuário da tentativa de autenticação',
    )

    autenticado = models.BooleanField(
        verbose_name='Autenticado',
        default=False,
        help_text='Se a tentativa de autenticação foi bem-sucedida ou não',
    )

    data_autenticacao = models.DateField(
        verbose_name='Data da autenticação',
        auto_now_add=True,
        help_text='Data da tentativa de autenticação',
    )

    hora_autenticacao = models.TimeField(
        verbose_name='Hora da autenticação',
        auto_now_add=True,
        help_text='Hora da tentativa de autenticação',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'log_autenticacao'
        verbose_name = 'Log de autenticação'
        verbose_name_plural = 'Logs de autenticação'

    def __str__(self):
        return f'{self.id} - {self.usuario} [{self.autenticado}]'
