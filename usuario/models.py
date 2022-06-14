from django.db import models
from django.apps import apps
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission
from django.contrib.auth.hashers import make_password
from core.validators import RegexTelefone, RegexCelular, RegexCodigoVerificacaoSegundaEtapa
from empresa.models import Empresa
from core.models import Base, get_uuid


Group.add_to_class(
    'uuid',
    models.UUIDField(
        verbose_name='UUID',
        default=get_uuid,
        help_text='UUID Código único não sequencial',
    )
)

Permission.add_to_class(
    'uuid',
    models.UUIDField(
        verbose_name='UUID',
        default=get_uuid,
        help_text='UUID Código único não sequencial',
    )
)


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


def serializador_codigo():
    ultimo_registro = Usuario.objects.all().order_by('id').last()

    if not ultimo_registro:
        return 1

    return int(ultimo_registro.codigo) + 1


class Usuario(AbstractUser):
    """
    Modelo de usuários do sistema, tanto dos usuários que vão abrir, quanto aos que vão solucionar os tickets. No caso
    dos usuários que vão soluciuonar os tickets, eles não vão ter nenhuma empresa vinculada a eles.
    """

    uuid = models.UUIDField(
        verbose_name='UUID',
        default=get_uuid,
        help_text='UUID Código único não sequencial',
    )

    """codigo = models.PositiveBigIntegerField(
        verbose_name='Código',
        default=serializador_codigo,
        unique=True,
        help_text='Código do usuário',
    )"""

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        help_text='Telefone fixo ex: 3100000000',
        validators=[
            RegexValidator(regex=RegexTelefone.get_regex(), message=RegexTelefone.get_mensagem()),
        ]
    )

    celular = models.CharField(
        verbose_name='Celular',
        max_length=11,
        default='',
        blank=True,
        help_text='Telefone celular ex: 31900000000',
        validators=[
            RegexValidator(regex=RegexCelular.get_regex(), message=RegexCelular.get_mensagem()),
        ]
    )

    classificacao = models.ForeignKey(
        'Classificacao',
        verbose_name='Classificação',
        related_name='classificacao_classificacao_usuario',
        null=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
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
        null=True,
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
        validators=[
            RegexValidator(regex=RegexCodigoVerificacaoSegundaEtapa.get_regex(),
                           message=RegexCodigoVerificacaoSegundaEtapa.get_mensagem()),
        ]
    )

    is_manager = models.BooleanField(
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
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        indexes = [
            models.Index(fields=['uuid'], name='idx_uuid_usr'),
            # models.Index(fields=['codigo'], name='idx_codigo_usr'),
            models.Index(fields=['empresa'], name='idx_empresa_usr'),
            models.Index(fields=['media_avaliacoes'], name='idx_media_avaliacoes_usr'),
        ]

    def __str__(self):
        return str(self.uuid)


class LogAutenticacao(models.Model):
    """
    Modelo que vai guardar as tentativas de login, tanto as que tiveram sucesso quanto as que falharem.
    """

    uuid = models.UUIDField(
        verbose_name='UUID',
        default=get_uuid,
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
        indexes = [
            models.Index(fields=['uuid'], name='idx_uuid_lgaut'),
            models.Index(fields=['ip'], name='idx_ip_lgaut'),
        ]

    def __str__(self):
        return str(self.uuid)


class Classificacao(Base):
    """
    Modelo da classificação dos usuários.
    """

    codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código da Classificação',
    )

    nome = models.CharField(
        verbose_name='Nome',
        max_length=255,
        help_text='Nome da classificação',
    )

    descricao = models.TextField(
        verbose_name='descricao',
        help_text='Descrição da classificação',
        blank=True,
        default='',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'classificacao'
        verbose_name = 'Classificacao'
        verbose_name_plural = 'Classificacoes'
        indexes = [
            models.Index(fields=['uuid'], name='idx_uuid_cls'),
            models.Index(fields=['codigo'], name='idx_codigo_cls'),
        ]

    def __str__(self):
        return str(self.uuid)

