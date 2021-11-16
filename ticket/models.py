from django.db import models
from core.models import Base
from usuario.models import Usuario


STATUS_CHOISES = [
    ('0', 'Aberto'),
    ('1', 'Processando'),
    ('2', 'Concluído'),
    ('3', 'Finalizado'),
    ('4', 'Cancelado'),
]


AVALIACAO_CHOISES = [
    ('1', 'Péssimo'),
    ('2', 'Ruim'),
    ('3', 'Bom'),
    ('4', 'Muito Bom'),
    ('5', 'Ótimo')
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

    avaliacao_solicitante = models.CharField(
        verbose_name='Avaliação do Solicitante',
        choices=AVALIACAO_CHOISES,
        max_length=1,
        help_text='Avaliação do solicitante referente ao chamado',
    )

    avaliacao_atendente = models.CharField(
        verbose_name='Avaliação do Atendente',
        choices=AVALIACAO_CHOISES,
        max_length=1,
        help_text='Avaliação do atendente referente ao chamado',
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
