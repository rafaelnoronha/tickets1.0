from django.db import models
from prestadora_servico.models import PrestadoraServico


class Empresa(PrestadoraServico):
    media_avaliacoes = models.DecimalField(
        verbose_name='Média das avaliações',
        max_digits=2,
        decimal_places=1,
        default=0,
        help_text='Média das avaliações dos chamados',
    )
