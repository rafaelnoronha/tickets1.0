import unicodedata
from django.db import models
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.utils.crypto import salted_hmac
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from core.validators import RegexTelefone, RegexCelular, RegexCodigoVerificacaoSegundaEtapa, UnicodeUsernameValidator
from core.models import Base
from empresa.models import Empresa
from agrupamento.models import Classificacao


class Usuario(AbstractBaseUser, Base):
    """
    Modelo de usuários do sistema, tanto dos usuários que vão abrir, quanto aos que vão solucionar os tickets. No caso
    dos usuários que vão soluciuonar os tickets, eles não vão ter nenhuma empresa vinculada a eles.
    """

    validador_nome_usuario = UnicodeUsernameValidator()

    sr_usuario = models.CharField(
        verbose_name='Usuário',
        max_length=150,
        unique=True,
        help_text='Nome único do usuário pelo qual efeturá login',
        validators=[validador_nome_usuario],
        error_messages={
            'unique': "Um usuário com esse nome já existe.",
        },
    )

    sr_senha = models.CharField(
        verbose_name='Senha',
        max_length=128
    )

    sr_nome = models.CharField(
        verbose_name='Nome',
        max_length=150,
        blank=True,
        help_text='Nome completo do usuário'
    )

    sr_email = models.EmailField(
        verbose_name='Email',
        blank=True,
        help_text='Email ex: email@exemplo.com.br'
    )

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
        Classificacao,
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

    sr_ultimo_login = models.DateTimeField(
        verbose_name='Último Login',
        blank=True,
        null=True
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

    sr_atendente = models.BooleanField(
        verbose_name='Atendente',
        default=False,
        help_text='Se é gerente, caso seja, existem privilégios padrões para um usuário do tipo gerente',
    )

    sr_gerente = models.BooleanField(
        verbose_name='Gerente',
        default=False,
        help_text='Este campo informa se o usuáio é gerente ou não',
    )

    sr_administrador = models.BooleanField(
        verbose_name='Administrador',
        default=False,
        help_text='Este campo informa se o usuáio é administrador ou não',
    )

    USERNAME_FIELD = 'sr_usuario'

    def set_password(self, raw_password):
        self.sr_senha = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.sr_password, setter)

    def set_unusable_password(self):
        # Set a value that will never be a valid hash
        self.sr_password = make_password(None)

    def has_usable_password(self):
        """
        Return False if set_unusable_password() has been called for this user.
        """
        return is_password_usable(self.sr_password)

    def _legacy_get_session_auth_hash(self):
        # RemovedInDjango40Warning: pre-Django 3.1 hashes will be invalid.
        key_salt = 'django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash'
        return salted_hmac(key_salt, self.sr_password, algorithm='sha1').hexdigest()

    def get_session_auth_hash(self):
        """
        Return an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(
            key_salt,
            self.sr_password,
            # RemovedInDjango40Warning: when the deprecation ends, replace
            # with:
            # algorithm='sha256',
            algorithm=settings.DEFAULT_HASHING_ALGORITHM,
        ).hexdigest()

    @classmethod
    def get_email_field_name(cls):
        try:
            return cls.EMAIL_FIELD
        except AttributeError:
            return 'sr_email'

    @classmethod
    def normalize_username(cls, username):
        return unicodedata.normalize('NFKC', username) if isinstance(username, str) else username

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
