from django.db import models
from core.models import Base, UF_CHOICES, PAISES_CHOISES


class Empresa(Base):
    cpf_cnpj = models.CharField(
        verbose_name='CPF/CNPJ',
        max_length=14,
        help_text='CPF ou CNPJ da empresa(apenas números)',
    )

    razao_social = models.CharField(
        verbose_name='Razão Social',
        max_length=60,
        help_text='Razão social(nome)',
    )

    nome_fantasia = models.CharField(
        verbose_name='Nome Fantasia',
        max_length=60,
        default='',
        help_text='Nome fantasia(apelido)',
    )

    logradouro = models.CharField(
        verbose_name='Logradouro',
        max_length=255,
        help_text='Logradouro/Endereço ex: Rua Direita',
    )

    numero = models.CharField(
        verbose_name='Número',
        max_length=60,
        help_text='Número do logradouro',
    )

    complemento = models.CharField(
        verbose_name='Complemento',
        max_length=60,
        default='',
        help_text='Complemento do endereço',
    )

    bairro = models.CharField(
        verbose_name='Bairro',
        max_length=60,
        help_text='Bairro',
    )

    municipio = models.CharField(
        verbose_name='Município',
        max_length=60,
        help_text='Município/Cidade',
    )

    uf = models.CharField(
        verbose_name='UF',
        max_length=2,
        choices=UF_CHOICES,
        help_text='UF ex: MG',
    )

    cep = models.CharField(
        verbose_name='CEP',
        max_length=8,
        help_text='CEP(apenas números)',
    )

    pais = models.CharField(
        verbose_name='País',
        max_length=60,
        choices=PAISES_CHOISES,
        help_text='Nome do pais',
    )

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        help_text='Número do telefone de contato(apenas números)',
    )

    media_avaliacoes = models.DecimalField(
        verbose_name='Média das avaliações',
        max_digits=2,
        decimal_places=1,
        default=0,
        help_text='Média das avaliações dos chamados',
    )

    prestadora = models.BooleanField(
        verbose_name='Prestadora',
        default=False,
        help_text='Se o cadastro da empresa será o cadastro da empresa que prestará os serviços',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f'{self.id} - {self.razao_social} - {self.cpf_cnpj} [{self.ativo}]'
