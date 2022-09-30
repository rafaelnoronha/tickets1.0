from django.db import models
from django.apps import apps
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from core.models import Base
from core.validators import RegexTelefone, RegexCelular, RegexCodigoVerificacaoSegundaEtapa
from empresa.models import Empresa


class GerenciadorUsuario(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class Usuario(AbstractUser):
    """
    Modelo de usuários do sistema, tanto dos usuários que vão abrir, quanto aos que vão solucionar os tickets. No caso
    dos usuários que vão soluciuonar os tickets, eles não vão ter nenhuma empresa vinculada a eles.
    """

    sr_telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        help_text='Telefone fixo ex: 3100000000',
        validators=[
            RegexValidator(regex=RegexTelefone.get_regex(), message=RegexTelefone.get_mensagem()),
        ]
    )

    sr_celular = models.CharField(
        verbose_name='Celular',
        max_length=11,
        blank=True,
        help_text='Telefone celular ex: 31900000000',
        validators=[
            RegexValidator(regex=RegexCelular.get_regex(), message=RegexCelular.get_mensagem()),
        ]
    )

    sr_classificacao = models.ForeignKey(
        'Classificacao',
        verbose_name='Classificação',
        related_name='rl_sr_classificacao',
        null=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
    )

    sr_media_avaliacoes = models.DecimalField(
        verbose_name='Média das avaliações',
        max_digits=2,
        decimal_places=1,
        default=0,
        help_text='Média das avaliações dos chamados avaliados',
    )

    sr_empresa = models.ForeignKey(
        Empresa,
        verbose_name='Empresa',
        related_name='rl_sr_empresa',
        on_delete=models.PROTECT,
        null=True,
        help_text='Empresa a qual o usuário pertence',
    )

    sr_observacoes = models.TextField(
        verbose_name='Observações',
        blank=True,
        help_text='Observações referênte ao usuário',
    )

    sr_numero_tentativas_login = models.PositiveSmallIntegerField(
        verbose_name='Número de tentativas falhas de login',
        default=0,
        help_text='Número de tentativas falhas ao fazer login',
    )

    sr_verificacao_duas_etapas = models.BooleanField(
        verbose_name='Verificação em duas etapas',
        default=False,
        help_text='Se deve exigir ou não a verificação da segunda etapa no login',
    )

    sr_codigo_verificacao_segunda_etapa = models.CharField(
        verbose_name='Código de verificação da segunda etapa',
        max_length=4,
        help_text='O código que valida a verificação da segunda etapa, como a senha ao fazer o login',
        validators=[
            RegexValidator(regex=RegexCodigoVerificacaoSegundaEtapa.get_regex(),
                           message=RegexCodigoVerificacaoSegundaEtapa.get_mensagem()),
        ]
    )

    sr_is_manager = models.BooleanField(
        verbose_name='Is Manager',
        default=False,
        help_text='Este campo informa se o usuáio é gerente ou não',
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

    objects = GerenciadorUsuario()

    class Meta:
        ordering = ['-id']
        db_table = 'tc_usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        indexes = [
            models.Index(fields=['sr_classificacao'], name='idx_sr_classificacao'),
            models.Index(fields=['sr_empresa'], name='idx_sr_empresa'),
            models.Index(fields=['sr_media_avaliacoes'], name='idx_sr_media_avaliacoes'),
        ]

    def __str__(self):
        return str(self.id)
