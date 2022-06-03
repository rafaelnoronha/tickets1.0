from django.dispatch import receiver
from django.db.models.signals import post_migrate
from usuario.models import Usuario


@receiver(post_migrate, sender=Usuario)
def post_migrate_usuario(sender, app_config, **kwargs):
    print('-> Executando o POST_MIGRATE no Usuario')
    print(kwargs)
    pass
