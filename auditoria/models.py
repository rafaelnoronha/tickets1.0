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


class LogAutenticacao(models.Model):
    """
    Modelo que vai guardar as tentativas de login, tanto as que tiveram sucesso quanto as que falharem.
    """

    lg_ip = models.GenericIPAddressField(
        verbose_name='IP',
        help_text='Endereço IP do cliente/dispositivo',
    )

    lg_usuario = models.ForeignKey(
        Usuario,
        verbose_name='Usuário',
        related_name='rl_lg_usuario',
        on_delete=models.PROTECT,
        help_text='Usuário da tentativa de autenticação',
    )

    lg_autenticado = models.BooleanField(
        verbose_name='Autenticado',
        default=False,
        help_text='Se a tentativa de autenticação foi bem-sucedida ou não',
    )

    lg_data_autenticacao = models.DateField(
        verbose_name='Data da autenticação',
        auto_now_add=True,
        help_text='Data da tentativa de autenticação',
    )

    lg_hora_autenticacao = models.TimeField(
        verbose_name='Hora da autenticação',
        auto_now_add=True,
        help_text='Hora da tentativa de autenticação',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'tc_log_autenticacao'
        verbose_name = 'Log de autenticação'
        verbose_name_plural = 'Logs de autenticação'
        indexes = [
            models.Index(fields=['lg_ip'], name='idx_lg_ip'),
            models.Index(fields=['lg_usuario'], name='idx_lg_usuario'),
        ]

    def __str__(self):
        return str(self.id)
