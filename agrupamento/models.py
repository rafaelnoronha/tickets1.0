from django.db import models
from core.models import Base


TIPO_CHOISES = [
    ('G', 'Grupo'),
    ('S', 'Subgrupo'),
]


class Agrupamento(Base):
    """
    Modelo de grupo e subgrupo dos tickets.
    """

    gr_codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código do Agrupamento',
    )

    gr_nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        help_text='Nome do Agrupamento',
    )

    gr_prioridade = models.PositiveSmallIntegerField(
        verbose_name='Prioridade',
        default=0,
        help_text='Prioridade do Agrupamento',
    )

    gr_tipo = models.CharField(
        verbose_name='Tipo',
        choices=TIPO_CHOISES,
        default='G',
        max_length=1,
        help_text='Tipo do Agrupamrento',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'tc_agrupamento'
        verbose_name = 'Agrupamento'
        verbose_name_plural = 'Agrupamentos'
        indexes = [
            models.Index(fields=['gr_tipo'], name='idx_gr_tipo'),
            models.Index(fields=['gr_codigo'], name='idx_gr_codigo'),
        ]

    def __str__(self):
        return str(self.id)


class Classificacao(Base):
    """
    Modelo da classificação dos usuários.
    """

    cl_codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código da Classificação',
    )

    cl_nome = models.CharField(
        verbose_name='Nome',
        max_length=50,
        help_text='Nome da classificação',
    )

    cl_descricao = models.TextField(
        verbose_name='descricao',
        help_text='Descrição da classificação',
        blank=True,
        default='',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'tc_classificacao'
        verbose_name = 'Classificacao'
        verbose_name_plural = 'Classificacoes'
        indexes = [
            models.Index(fields=['cl_codigo'], name='idx_cl_codigo'),
        ]

    def __str__(self):
        return str(self.id)
