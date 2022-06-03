from django.apps import AppConfig


class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import core.signals
        # noinspection PyUnresolvedReferences
        import usuario.signals
