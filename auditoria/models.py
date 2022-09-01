from django.db import models
from usuario.models import Usuario


TIPO_OPERACAO_CHOISES = [
    ('CREATE', 'CREATE'),
    ('UPDATE', 'UPDATE'),
    ('DELETE', 'DELETE')
]


class Auditoria(models.Model):
    """
    Modelo responsável por gravar as operações realizadas no sistema.
    """

    data_operacao = models.DateField(
        verbose_name='Data da Operação',
        auto_now_add=True,
        help_text='Data da execução da operação',
    )

    hora_operacao = models.TimeField(
        verbose_name='Hora da Operação',
        auto_now_add=True,
        help_text='Hora da execução da operação',
    )

    tabela_operacao = models.CharField(
        verbose_name='Tabela da Operação',
        max_length=100,
        help_text='Tabela onde ocorreu a operação',
    )

    tipo_operacao = models.CharField(
        verbose_name='Tipo de Operação',
        choices=TIPO_OPERACAO_CHOISES,
        max_length=6,
        help_text='Tipo de operação realizada',
    )

    usuario_operacao = models.ForeignKey(
        Usuario,
        verbose_name='Usuário da Operação',
        on_delete=models.PROTECT,
        related_name='usuario_operacao_usuario_auditoria',
        help_text='Usuário responsável pela operação realizada',
    )

    estado_anterior = models.TextField(
        verbose_name='Estado Anterior',
        default='',
        help_text='Estado anterior do registro afetado',
    )

    estado_atual = models.TextField(
        verbose_name='Estado Atual',
        default='',
        help_text='Estado atual do registro afetado',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'auditoria'
        verbose_name = 'Auditoria'
        verbose_name_plural = 'Auditoria'
        indexes = [
            models.Index(fields=['tabela_operacao'], name='idx_tabela_operacao_audt'),
            models.Index(fields=['tipo_operacao'], name='idx_tipo_operacao_audt'),
            models.Index(fields=['usuario_operacao'], name='idx_usuario_operacao_audt'),
        ]

    def __str__(self):
        return str(self.id)
