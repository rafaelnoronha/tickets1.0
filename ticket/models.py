from django.db import models
from core.models import Base
from usuario.models import Usuario
from agrupamento.models import Grupo, Subgrupo

STATUS_CHOISES = [
    ('0', 'Aberto'),
    ('1', 'Processando'),
    ('2', 'Concluído'),
    ('3', 'Finalizado'),
    ('4', 'Cancelado'),
]

AVALIACAO_CHOISES = [
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

    solicitante = models.ForeignKey(
        Usuario,
        verbose_name='Solicitante',
        related_name='solicitante_usuario_ticket',
        on_delete=models.PROTECT,
        help_text='Solicitante/Cliente responsável pelo ticket'
    )

    atendente = models.ForeignKey(
        Usuario,
        verbose_name='Atendente',
        related_name='atendente_usuario_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Atendente/Técnico responsável pelo ticket'
    )

    data_atribuicao_atendente = models.DateField(
        verbose_name='Data de atribuição do atendente',
        null=True,
        help_text='Data em que foi atribuído o atendente ao ticket',
    )

    hora_atribuicao_atendente = models.TimeField(
        verbose_name='Hora de atribuição do atendente',
        null=True,
        help_text='Hora em que foi atribuído o atendente ao ticket',
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
        null=True,
        help_text='Avaliação do solicitante referente ao chamado',
    )

    observacao_avaliacao_solicitante = models.TextField(
        verbose_name='Observação Avaliação do Solicitante',
        help_text='Observações referente à avaliação do solicitante',
        default='',
    )

    avaliacao_atendente = models.SmallIntegerField(
        verbose_name='Avaliação do Atendente',
        choices=AVALIACAO_CHOISES,
        null=True,
        help_text='Avaliação do atendente referente ao chamado',
    )

    observacao_avaliacao_atendente = models.TextField(
        verbose_name='Observação Avaliação do Atendente',
        help_text='Observações referente à avaliação do atendente',
        default='',
    )

    solucao = models.ForeignKey(
        MensagemTicket,
        verbose_name='Solução',
        related_name='solucao_ticket_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Mensagem de solução do ticket',
    )

    data_solucao = models.DateField(
        verbose_name='Data da Solução do Ticket',
        null=True,
        help_text='Data que o ticket foi solucionado',
    )

    hora_solucao = models.TimeField(
        verbose_name='Hora da Solução do Ticket',
        null=True,
        help_text='Hora que o ticket foi solucionado',
    )

    finalizado = models.ForeignKey(
        Usuario,
        verbose_name='Finalizado',
        related_name='finalizado_ticket_ticket',
        null=True,
        on_delete=models.PROTECT,
        help_text='Usuário que finalizou o ticket',
    )

    data_finalizacao = models.DateField(
        verbose_name='Data da Finalização do Ticket',
        null=True,
        help_text='Data que o ticket foi finalizado',
    )

    hora_finalizacao = models.TimeField(
        verbose_name='Hora da Finalização do Ticket',
        null=True,
        help_text='Hora que o ticket foi finalizado',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return f'{self.id} - {self.titulo} [{self.status}]'


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

    def __str__(self):
        return f'{self.id} - {self.ticket} [{self.usuario}]'
