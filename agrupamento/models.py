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

    codigo = models.CharField(
        verbose_name='Código',
        max_length=20,
        unique=True,
        help_text='Código do Agrupamento',
    )

    nome = models.CharField(
        verbose_name='Nome',
        max_length=60,
        help_text='Nome do Agrupamento',
    )

    prioridade = models.PositiveSmallIntegerField(
        verbose_name='Prioridade',
        default=0,
        help_text='Prioridade do Agrupamento',
    )

    tipo = models.CharField(
        verbose_name='Tipo',
        choices=TIPO_CHOISES,
        default='G',
        max_length=1,
        help_text='Tipo do Agrupamrento',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'agrupamento'
        verbose_name = 'Agrupamento'
        verbose_name_plural = 'Agrupamentos'
        indexes = [
            models.Index(fields=['tipo'], name='idx_gr_tipo'),
            models.Index(fields=['codigo'], name='idx_gr_codigo'),
        ]

    def __str__(self):
        return str(self.id)
