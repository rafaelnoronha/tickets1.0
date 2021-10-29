from django.db import models
from core.models import Base
from usuarios.models import Usuario


class PoliticaPrivacidade(Base):
    TIPO_TITULAR_CHOISES = [
        ('U', 'USUÁRIO'),
        ('E', 'EMPRESA'),
    ]

    tipo_titular = models.CharField(
        verbose_name='Tipo de Titular',
        max_length=1,
        choices=TIPO_TITULAR_CHOISES,
        help_text='Para qual tipo de titular a polítiva será requerida',
    )

    politica_privacidade = models.TextField(
        verbose_name='Política de Privacidade',
        help_text='O conteúdo da política de privacidade',
    )

    data_validade = models.DateField(
        verbose_name='Data de Validade',
        help_text='Data da vigência da política de privacidade',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'politica_privacidade'
        verbose_name = 'Política de Privacidade'
        verbose_name_plural = 'Políticas de Privacidades'

    def __str__(self):
        return f'{self.id} - {self.data_validade}'


class ConsentimentoPoliticaPrivacidade(Base):
    titular = models.ForeignKey(
        Usuario,
        verbose_name='Consentimento da Política de Privacidade',
        related_name='usuario',
        on_delete=models.PROTECT,
        help_text='Usuário que concentiu ou não com a política de privacidade',
    )

    politica_privacidade = models.ForeignKey(
        PoliticaPrivacidade,
        verbose_name='Política de Privacidade',
        related_name='politica_privacidade',
        on_delete=models.PROTECT,
        help_text='Política de privacidade que o usuário consentiu ou não'
    )

    consentimento = models.BooleanField(
        verbose_name='Consentimento',
        default=False,
        help_text='Consentimento ou não do usuário, onde o consentimento = True e o não consentimento = False',
    )
