from .models import Ticket
from django.dispatch import receiver
from django.db.models.signals import pre_save
from datetime import datetime


@receiver(pre_save, sender=Ticket)
def antes_de_salvar_ticket(sender, instance, **kwargs):
    prioridade_grupo = instance.grupo.prioridade if instance.grupo else 0
    prioridade_subgrupo = instance.subgrupo.prioridade if instance.subgrupo else 0

    instance.prioridade = prioridade_grupo + prioridade_subgrupo

    if instance.atendente:
        instance.data_atribuicao_atendente = datetime.today().strftime('%Y-%m-%d')
        instance.hora_atribuicao_atendente = datetime.today().strftime('%H:%M:%S')

    if instance.finalizado:
        instance.data_finalizacao = datetime.today().strftime('%Y-%m-%d')
        instance.hora_finalizacao = datetime.today().strftime('%H:%M:%S')
