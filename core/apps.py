from django.apps import AppConfig
from django.db.models.signals import pre_migrate
from .signals import post_migrate_triggers


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        pre_migrate.connect(post_migrate_triggers, self)
