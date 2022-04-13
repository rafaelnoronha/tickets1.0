from .models import Empresa
from django.core.exceptions import ValidationError

from django.dispatch import receiver
from django.db.models.signals import pre_save


@receiver(pre_save, sender=Empresa)
def antes_de_salvar_empresa(sender, instance, **kwargs):
    pass
