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

    class Meta:
        ordering = ['-id']
        db_table = 'empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f'{self.id} - {self.razao_social} - {self.cpf_cnpj} [{self.ativo}]'
