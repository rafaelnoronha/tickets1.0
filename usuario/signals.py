from .models import Usuario
from auditoria.models import Auditoria
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


@receiver(pre_save, sender=Usuario)
def antes_de_salvar_usuario(sender, instance, **kwargs):
    instance.set_password(instance.password)


@receiver(post_save, sender=Usuario)
def depois_de_salvar_usuario(sender, instance, **kwargs):
    #
    pass