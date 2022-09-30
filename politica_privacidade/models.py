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

    pl_codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código da política de privacidade',
    )

    pl_titulo = models.CharField(
        verbose_name='Título da Política de Privacidade',
        max_length=100,
        help_text='Título da política de privacidade',
    )

    pl_descricao = models.TextField(
        verbose_name='Descrição',
        help_text='A descrição/conteúdo da política de privacidade',
    )

    pl_tipo_titular = models.CharField(
        verbose_name='Tipo de Titular',
        max_length=1,
        choices=TIPO_TITULAR_CHOISES,
        help_text='Para qual tipo de titular a polítiva será requerida',
    )

    pl_data_validade = models.DateField(
        verbose_name='Data de Validade',
        help_text='Data da vigência da política de privacidade',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'tc_politica_privacidade'
        verbose_name = 'Política de Privacidade'
        verbose_name_plural = 'Políticas de Privacidade'
        indexes = [
            models.Index(fields=['pl_codigo'], name='idx_pl_codigo'),
        ]

    def __str__(self):
        return str(self.id)


class ConsentimentoPoliticaPrivacidade(Base):
    """
    Modelo que vai gravar os consentimentos e os não consentimentos das políticas de privacidades.
    """

    cn_titular = models.ForeignKey(
        Usuario,
        verbose_name='Consentimento da Política de Privacidade',
        related_name='rl_cn_titular',
        on_delete=models.PROTECT,
        help_text='Usuário que concentiu ou não com a política de privacidade',
    )

    cn_politica_privacidade = models.ForeignKey(
        PoliticaPrivacidade,
        verbose_name='Política de Privacidade',
        related_name='rl_cn_politica_privacidade',
        on_delete=models.PROTECT,
        help_text='Política de privacidade que o usuário consentiu ou não'
    )

    cn_consentimento = models.BooleanField(
        verbose_name='Consentimento',
        help_text='Consentimento ou não do usuário, onde o consentimento = True e o não consentimento = False',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'tc_consentimento_politica_privacidade'
        verbose_name = 'Consentimento da Política de Privacidade'
        verbose_name_plural = 'Consentimentos das Políticas de Privacidade'
        indexes = [
            models.Index(fields=['cn_politica_privacidade'], name='idx_cn_politica_privacidade'),
            models.Index(fields=['cn_titular'], name='idx_cn_titular'),
        ]

    def __str__(self):
        return str(self.id)
