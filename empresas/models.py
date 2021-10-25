from django.db import models
from core.models import Base


class Empresa(Base):
    UF_CHOICES = [
        ('RO', 'RO'),
        ('AC', 'AC'),
        ('AM', 'AM'),
        ('RR', 'RR'),
        ('PA', 'PA'),
        ('AP', 'AP'),
        ('TO', 'TO'),
        ('MA', 'MA'),
        ('PI', 'PI'),
        ('CE', 'CE'),
        ('RN', 'RN'),
        ('PB', 'PB'),
        ('PE', 'PE'),
        ('AL', 'AL'),
        ('SE', 'SE'),
        ('BA', 'BA'),
        ('MG', 'MG'),
        ('ES', 'ES'),
        ('RJ', 'RJ'),
        ('SP', 'SP'),
        ('PR', 'PR'),
        ('SC', 'SC'),
        ('RS', 'RS'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('GO', 'GO'),
        ('DF', 'DF'),
    ]

    cpf_cnpj = models.CharField(
        verbose_name='CPF/CNPJ',
        max_length=14,
    )

    razao_social = models.CharField(
        verbose_name='Razão Social',
        max_length=60,
    )

    nome_fantasia = models.CharField(
        verbose_name='Nome Fantasia',
        max_length=60,
        default='',
    )

    logradouro = models.CharField(
        verbose_name='Logradouro',
        max_length=255,
    )

    numero = models.CharField(
        verbose_name='Número',
        max_length=60,
    )

    complemento = models.CharField(
        verbose_name='Complemento',
        max_length=60,
        default='',
    )

    bairro = models.CharField(
        verbose_name='Bairro',
        max_length=60,
    )

    municipio = models.CharField(
        verbose_name='Município',
        max_length=60,
    )

    uf = models.CharField(
        verbose_name='UF',
        max_length=2,
        choices=UF_CHOICES,
    )

    cep = models.CharField(
        verbose_name='CEP',
        max_length=8,
    )

    pais = models.CharField(
        verbose_name='País',
        max_length=60,
    )

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
    )

    media_avaliacoes = models.DecimalField(
        verbose_name='Média das avaliações',
        max_digits=2,
        decimal_places=1,
        default=0,
    )

    class Meta:
        db_table = 'empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f'{self.id} - {self.razao_social} [{self.cpf_cnpj}]'
