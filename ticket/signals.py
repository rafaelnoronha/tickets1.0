from .models import Ticket
from django.dispatch import receiver
from django.db.models.signals import pre_save
from datetime import datetime


@receiver(pre_save, sender=Ticket)
def antes_de_salvar_ticket(sender, instance, **kwargs):
    if instance.atendente:
        instance.data_atribuicao_atendente = datetime.today().strftime('%Y-%m-%d')
        instance.hora_atribuicao_atendente = datetime.today().strftime('%H:%M:%S')
