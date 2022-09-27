from django.db import models
from core.models import Base
from usuario.models import Usuario, Classificacao
from agrupamento.models import Agrupamento


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
        related_name='rl_tc_solicitante',
        on_delete=models.PROTECT,
        help_text='Solicitante/Cliente responsável pelo ticket'
    )

    classificacao_atendente = models.ForeignKey(
        Classificacao,
        verbose_name='Classificação do Atendente',
        related_name='rl_tc_classificacao_atendente',
        null=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
    )

    atendente = models.ForeignKey(
        Usuario,
        verbose_name='Atendente',
        related_name='rl_tc_atendente',
        null=True,
        on_delete=models.PROTECT,
        help_text='Atendente/Técnico responsável pelo ticket'
    )

    titulo = models.CharField(
        verbose_name='Título',
        max_length=100,
        help_text='Título do ticket',
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        help_text='Descrição do ticket',
    )

    grupo = models.ForeignKey(
        Agrupamento,
        verbose_name='Grupo',
        related_name='rl_tc_grupo',
        null=True,
        on_delete=models.PROTECT,
        help_text='Grupo de classificação do ticket',
    )

    subgrupo = models.ForeignKey(
        Agrupamento,
        verbose_name='Subgrupo',
        related_name='rl_tc_subgrupo',
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

    class Meta:
        ordering = ['-id']
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        indexes = [
            models.Index(fields=['status'], name='idx_tc_status'),
            models.Index(fields=['prioridade'], name='idx_tc_prioridade'),
            models.Index(fields=['solicitante'], name='idx_tc_solicitante'),
            models.Index(fields=['atendente'], name='idx_tc_atendente'),
            models.Index(fields=['classificacao_atendente'], name='idx_tc_classificacao_atendente'),
            models.Index(fields=['avaliacao_solicitante'], name='idx_tc_avaliacao_solicitante'),
            models.Index(fields=['grupo'], name='idx_tc_grupo'),
            models.Index(fields=['subgrupo'], name='idx_tc_subgrupo'),
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
        related_name='rl_mn_usuario',
        on_delete=models.PROTECT,
        help_text='Usuário autor(remetente) da mensagem',
    )

    ticket = models.ForeignKey(
        Ticket,
        verbose_name='Ticket',
        related_name='rl_mn_ticket',
        on_delete=models.CASCADE,
        help_text='Ticket que receberá a mensagem',
    )

    mensagem = models.TextField(
        verbose_name='Mensagem',
        help_text='Conteúdo da mensagem',
    )

    mensagem_relacionada = models.ForeignKey(
        'self',
        related_name='rl_mn_mensagem_relacionada',
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
            models.Index(fields=['ticket'], name='idx_mn_ticket'),
            models.Index(fields=['usuario'], name='idx_mn_usuario'),
            models.Index(fields=['mensagem_relacionada'], name='idx_mn_mensagem_relacionada'),
        ]

    def __str__(self):
        return str(self.id)


class MovimentoTicket(Base):
    ticket = models.ForeignKey(
        Ticket,
        verbose_name='Ticket',
        related_name='rl_mv_ticket',
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
        related_name='rl_mv_atendente',
        null=True,
        on_delete=models.PROTECT,
        help_text='Atendente/Técnico responsável pelo ticket'
    )

    classificacao_atendente = models.ForeignKey(
        Classificacao,
        verbose_name='Classificação do Atendente',
        related_name='rl_mv_classificacao_atendente',
        null=True,
        on_delete=models.PROTECT,
        help_text='A qual classificação de usuário o ticket é designado'
    )


    solucao = models.ForeignKey(
        'MensagemTicket',
        verbose_name='Solução',
        related_name='rl_mv_solucao',
        null=True,
        on_delete=models.PROTECT,
        help_text='Solução do ticket',
    )

    finalizado = models.ForeignKey(
        Usuario,
        verbose_name='Finalizado',
        related_name='rl_mv_finalizado',
        null=True,
        on_delete=models.PROTECT,
        help_text='Usuário que finalizou o ticket',
    )

    cancelado = models.ForeignKey(
        Usuario,
        verbose_name='Cancelado',
        related_name='rl_mv_cancelado',
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
        db_table = 'movimento_ticket'
        verbose_name = 'Movimento do Ticket'
        verbose_name_plural = 'Movimentos do Ticket'
        indexes = [
            models.Index(fields=['ticket'], name='idx_mv_ticket'),
            models.Index(fields=['atendente'], name='idx_mv_atendente'),
            models.Index(fields=['classificacao_atendente'], name='idx_mv_classificacao_atendente'),
            models.Index(fields=['finalizado'], name='idx_mv_finalizado'),
            models.Index(fields=['cancelado'], name='idx_mv_cancelado'),
            models.Index(fields=['solucao'], name='idx_mv_solucao'),
        ]

    def __str__(self):
        return str(self.id)
