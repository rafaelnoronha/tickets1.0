from django.db import models
from core.models import Base
from usuario.models import Usuario


TIPO_TITULAR_CHOISES = [
    ('U', 'USUÁRIO'),
    ('E', 'EMPRESA'),
]


class PoliticaPrivacidade(Base):
    """
    Modelo que vai gerenciar as políticas de privacidade.
    """

    codigo = models.CharField(
        verbose_name='Código',
        max_length=150,
        unique=True,
        help_text='Código da política de privacidade',
    )

    titulo = models.CharField(
        verbose_name='Título da Política de Privacidade',
        max_length=150,
        help_text='Título da política de privacidade',
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        help_text='A descrição/conteúdo da política de privacidade',
    )

    tipo_titular = models.CharField(
        verbose_name='Tipo de Titular',
        max_length=1,
        choices=TIPO_TITULAR_CHOISES,
        help_text='Para qual tipo de titular a polítiva será requerida',
    )

    data_validade = models.DateField(
        verbose_name='Data de Validade',
        help_text='Data da vigência da política de privacidade',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'politica_privacidade'
        verbose_name = 'Política de Privacidade'
        verbose_name_plural = 'Políticas de Privacidade'
        indexes = [
            models.Index(fields=['codigo'], name='idx_codigo_pop'),
        ]

    def __str__(self):
        return str(self.id)


class ConsentimentoPoliticaPrivacidade(Base):
    """
    Modelo que vai gravar os consentimentos e os não consentimentos das políticas de privacidades.
    """

    titular = models.ForeignKey(
        Usuario,
        verbose_name='Consentimento da Política de Privacidade',
        related_name='titular_usuario_consentimento_politica_privacidade',
        on_delete=models.PROTECT,
        help_text='Usuário que concentiu ou não com a política de privacidade',
    )

    politica_privacidade = models.ForeignKey(
        PoliticaPrivacidade,
        verbose_name='Política de Privacidade',
        related_name='politica_privacidade_politica_privacidade_consentimento_politica_privacidade',
        on_delete=models.PROTECT,
        help_text='Política de privacidade que o usuário consentiu ou não'
    )

    consentimento = models.BooleanField(
        verbose_name='Consentimento',
        help_text='Consentimento ou não do usuário, onde o consentimento = True e o não consentimento = False',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'consentimento_politica_privacidade'
        verbose_name = 'Consentimento da Política de Privacidade'
        verbose_name_plural = 'Consentimentos das Políticas de Privacidade'
        indexes = [
            models.Index(fields=['politica_privacidade'], name='idx_politica_privacidade_cpop'),
            models.Index(fields=['consentimento'], name='idx_consentimento_cpop'),
        ]

    def __str__(self):
        return str(self.id)
