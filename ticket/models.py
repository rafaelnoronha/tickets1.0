from django.db import models
from core.models import Base
from usuario.models import Usuario, Classificacao
from agrupamento.models import Grupo, Subgrupo


STATUS_CHOISES = [
    ('0', 'Aberto'),
    ('1', 'Processando'),
    ('2', 'Solucionado'),
    ('3', 'Finalizado'),
    ('4', 'Cancelado'),
]

AVALIACAO_CHOISES = [
    (0, 'Não Avaliado'),
    (1, 'Péssimo'),
    (2, 'Ruim'),
    (3, 'Bom'),
    (4, 'Muito Bom'),
    (5, 'Ótimo')
]


class Ticket(Base):
    """
    Modelo dos tickets, em específico do cabeçalho dos tickets, sem as mensagens/acompanhamentos.
    """

    status = models.CharField(
        verbose_name='Status',
        choices=STATUS_CHOISES,
        max_length=1,
        default='0',
        help_text='Status do ticket',
    )

    prioridade = models.PositiveSmallIntegerField(
        verbose_name='Prioridade',
        default=0,
        help_text='Prioridade de atendimento do ticket',
    )

    solicitante = models.ForeignKey(
        Usuario,
        verbose_name='Solicitante',
        related_name='solicitante_usuario_ticket',
        on_delete=models.PROTECT,
        help_text='Solicitante/Cliente responsável pelo ticket'
    )

    classificacao_atendente = models.ForeignKey(
        Classificacao,
        verbose_name='Classificação do Atendente',
        related_name='classificacao_atendente_usuario_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
    )

    atendente = models.ForeignKey(
        Usuario,
        verbose_name='Atendente',
        related_name='atendente_usuario_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Atendente/Técnico responsável pelo ticket'
    )

    titulo = models.CharField(
        verbose_name='Título',
        max_length=255,
        help_text='Título do ticket',
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        help_text='Descrição do ticket',
    )

    grupo = models.ForeignKey(
        Grupo,
        verbose_name='Grupo',
        related_name='grupo_agrupamento_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Grupo de classificação do ticket',
    )

    subgrupo = models.ForeignKey(
        Subgrupo,
        verbose_name='Subgrupo',
        related_name='subgrupo_agrupamento_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Subgrupo de classificação do ticket',
    )

    avaliacao_solicitante = models.SmallIntegerField(
        verbose_name='Avaliação do Solicitante',
        choices=AVALIACAO_CHOISES,
        default=0,
        help_text='Avaliação do solicitante referente ao chamado',
    )

    observacao_avaliacao_solicitante = models.TextField(
        verbose_name='Observação Avaliação do Solicitante',
        help_text='Observações referente à avaliação do solicitante',
        blank=True,
    )

    solucionado = models.ForeignKey(
        'MensagemTicket',
        verbose_name='Solucionado',
        related_name='solucionado_ticket_mensagem_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Mensagem de solução do ticket',
    )

    finalizado = models.ForeignKey(
        Usuario,
        verbose_name='Finalizado',
        related_name='finalizado_ticket_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Usuário que finalizou o ticket',
    )

    cancelado = models.ForeignKey(
        Usuario,
        verbose_name='Cancelado',
        related_name='cancelado_ticket_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Usuário que finalizou o ticket',
    )

    motivo_cancelamento = models.TextField(
        verbose_name='Motivo do Cancelamento',
        help_text='Motivo/Justificativa do cancelamento do ticket',
        blank=True,
    )

    class Meta:
        ordering = ['-id']
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        indexes = [
            models.Index(fields=['status'], name='idx_status_tik'),
            models.Index(fields=['prioridade'], name='idx_prioridade_tik'),
            models.Index(fields=['solicitante'], name='idx_solicitante_tik'),
            models.Index(fields=['atendente'], name='idx_atendente_tik'),
            models.Index(fields=['avaliacao_solicitante'], name='idx_avaliacao_solicitante_tik'),
            models.Index(fields=['grupo'], name='idx_grupo_tik'),
            models.Index(fields=['subgrupo'], name='idx_subgrupo_tik'),
            models.Index(fields=['finalizado'], name='idx_finalizado_tik'),
            models.Index(fields=['cancelado'], name='idx_cancelado_tik'),
        ]

    def __str__(self):
        return str(self.id)


class MensagemTicket(Base):
    """
    Modelo das mensagens/acompanhemento dos tickets.
    """

    usuario = models.ForeignKey(
        Usuario,
        verbose_name='Usuário',
        related_name='usuario_usuario_mensagem_ticket',
        on_delete=models.PROTECT,
        help_text='Usuário autor(remetente) da mensagem',
    )

    ticket = models.ForeignKey(
        Ticket,
        verbose_name='Ticket',
        related_name='ticket_ticket_mensagem_ticket',
        on_delete=models.CASCADE,
        help_text='Ticket que receberá a mensagem',
    )

    mensagem = models.TextField(
        verbose_name='Mensagem',
        help_text='Conteúdo da mensagem',
    )

    mensagem_relacionada = models.ForeignKey(
        'self',
        related_name='mensagem_relacionada_mensagem_ticket_mensagem_ticket',
        on_delete=models.CASCADE,
        null=True,
        help_text='Mensagem a qual a mensagem atual estará vinculada como resposta',
    )

    solucao = models.BooleanField(
        verbose_name='Solução',
        default=False,
        help_text='Informa se a mensagem é uma solução para o ticket aberto',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'mensagem_ticket'
        verbose_name = 'Mensagem do Ticket'
        verbose_name_plural = 'Mensagens do Ticket'
        indexes = [
            models.Index(fields=['ticket'], name='idx_ticket_mtik'),
            models.Index(fields=['usuario'], name='idx_usuario_mtik'),
            models.Index(fields=['solucao'], name='idx_solucao_mtik'),
        ]

    def __str__(self):
        return str(self.id)


class MovimentoTicket(Base):
    ticket = models.ForeignKey(
        Ticket,
        verbose_name='Ticket',
        related_name='ticket_ticket_movimento_ticket',
        on_delete=models.PROTECT,
        help_text='Ticket responsável pela movimentação'
    )

    data_inicio = models.DateField(
        verbose_name='Data de Início',
        null=True,
        help_text='Data que o ticket foi atribuido pela primeira vez',
    )

    hora_inicio = models.TimeField(
        verbose_name='Hora de Início',
        null=True,
        help_text='Hora em que o ticket foi atribuido pela primeira vez'
    )

    data_fim = models.DateField(
        verbose_name='Data de Finalizacao',
        null=True,
        help_text='Data que o ticket foi finalizado',
    )

    hora_fim = models.TimeField(
        verbose_name='Hora do Fim',
        null=True,
        help_text='Hora em que o ticket foi finalizado'
    )

    atendente = models.ForeignKey(
        Usuario,
        verbose_name='Atendente',
        related_name='atendente_usuario_movimento_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Atendente/Técnico responsável pelo ticket'
    )

    classificacao_atendente = models.ForeignKey(
        Classificacao,
        verbose_name='Classificação do Atendente',
        related_name='classificacao_atendente_usuario_movimento_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
    )

    solucionado = models.ForeignKey(
        'MensagemTicket',
        verbose_name='Solucionado',
        related_name='solucao_ticket_movimento_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Mensagem de solução do ticket',
    )

    finalizado = models.ForeignKey(
        Usuario,
        verbose_name='Finalizado',
        related_name='finalizado_ticket_movimento_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Usuário que finalizou o ticket',
    )

    cancelado = models.ForeignKey(
        Usuario,
        verbose_name='Cancelado',
        related_name='cancelado_ticket_movimento_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Usuário que finalizou o ticket',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'movimento_ticket'
        verbose_name = 'Movimento do Ticket'
        verbose_name_plural = 'Movimentos do Ticket'
        indexes = [
            models.Index(fields=['ticket'], name='idx_ticket_movtik'),
            models.Index(fields=['atendente'], name='idx_atendente_movtik'),
            models.Index(fields=['finalizado'], name='idx_finalizado_movtik'),
            models.Index(fields=['cancelado'], name='idx_cancelado_movtik'),
        ]

    def __str__(self):
        return str(self.id)
