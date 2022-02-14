from django.db import models
from core.models import Base


class Grupo(Base):
    """
    Modelo dos grupos dos tickets.
    """

    nome = models.CharField(
        verbose_name='Nome',
        max_length=255,
        help_text='Nome do Grupo',
    )

    peso = models.PositiveSmallIntegerField(
        verbose_name='Peso',
        default=0,
        help_text='Peso do Grupo',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'grupo'
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return f'{self.id} - {self.nome}'


class Subgrupo(Base):
    """
    Modelo dos subgrupos dos tickets.
    """

    nome = models.CharField(
        verbose_name='Nome',
        max_length=255,
        help_text='Nome do Subgrupo',
    )

    peso = models.PositiveSmallIntegerField(
        verbose_name='Peso',
        default=0,
        help_text='Peso do Subgrupo',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'subgrupo'
        verbose_name = 'Subgrupo'
        verbose_name_plural = 'Subgrupos'

    def __str__(self):
        return f'{self.id} - {self.nome}'
