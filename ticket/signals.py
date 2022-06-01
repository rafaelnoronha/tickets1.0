from .models import Ticket, MensagemTicket
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from datetime import datetime


@receiver(pre_save, sender=Ticket)
def pre_save_ticket(sender, instance, **kwargs):
    ticket_antigo = Ticket.objects.get(id=instance.id) if instance.id else None

    prioridade_grupo = instance.grupo.prioridade if instance.grupo else 0
    prioridade_subgrupo = instance.subgrupo.prioridade if instance.subgrupo else 0

    instance.prioridade = prioridade_grupo + prioridade_subgrupo

    if ticket_antigo:
        if not ticket_antigo.atendente and instance.atendente:
            instance.data_atribuicao_atendente = datetime.today().strftime('%Y-%m-%d')
            instance.hora_atribuicao_atendente = datetime.today().strftime('%H:%M:%S')

        if instance.solucionado:
            instance.data_solucao = datetime.today().strftime('%Y-%m-%d')
            instance.hora_solucao = datetime.today().strftime('%H:%M:%S')

        elif not instance.solucionado:
            instance.data_solucao = None
            instance.hora_solucao = None

    else:
        if instance.atendente:
            instance.data_atribuicao_atendente = datetime.today().strftime('%Y-%m-%d')
            instance.hora_atribuicao_atendente = datetime.today().strftime('%H:%M:%S')


@receiver(post_save, sender=MensagemTicket)
def pre_save_mensagem_ticket(sender, instance, created, **kwargs):
    if instance.solucao:
        ticket = instance.ticket
        ticket.solucionado = instance
        ticket.data_solucao = datetime.today().strftime('%Y-%m-%d')
        ticket.hora_solucao = datetime.today().strftime('%H:%M:%S')
        ticket.save()
