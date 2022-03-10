from .models import Usuario
from django.dispatch import receiver
from django.db.models.signals import pre_save


@receiver(pre_save, sender=Usuario)
def antes_de_salvar_usuario(sender, instance, **kwargs):
    instance.set_password(instance.password)
