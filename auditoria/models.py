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

    dt_data_operacao = models.DateField(
        verbose_name='Data da Operação',
        auto_now_add=True,
        help_text='Data da execução da operação',
    )

    dt_hora_operacao = models.TimeField(
        verbose_name='Hora da Operação',
        auto_now_add=True,
        help_text='Hora da execução da operação',
    )

    dt_tabela_operacao = models.CharField(
        verbose_name='Tabela da Operação',
        max_length=100,
        help_text='Tabela onde ocorreu a operação',
    )

    dt_tipo_operacao = models.CharField(
        verbose_name='Tipo de Operação',
        choices=TIPO_OPERACAO_CHOISES,
        max_length=6,
        help_text='Tipo de operação realizada',
    )

    dt_usuario_operacao = models.ForeignKey(
        Usuario,
        verbose_name='Usuário da Operação',
        on_delete=models.PROTECT,
        related_name='rl_dt_usuario_operacao',
        help_text='Usuário responsável pela operação realizada',
    )

    dt_estado_anterior = models.TextField(
        verbose_name='Estado Anterior',
        default='',
        help_text='Estado anterior do registro afetado',
    )

    dt_estado_atual = models.TextField(
        verbose_name='Estado Atual',
        default='',
        help_text='Estado atual do registro afetado',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'tc_auditoria'
        verbose_name = 'Auditoria'
        verbose_name_plural = 'Auditoria'
        indexes = [
            models.Index(fields=['dt_tabela_operacao'], name='idx_dt_tabela_operacao'),
            models.Index(fields=['dt_tipo_operacao'], name='idx_dt_tipo_operacao'),
            models.Index(fields=['dt_usuario_operacao'], name='idx_dt_usuario_operacao'),
        ]

    def __str__(self):
        return str(self.id)
