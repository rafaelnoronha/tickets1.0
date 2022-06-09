from django.apps import AppConfig
from django.db.models.signals import pre_migrate, post_migrate
from .signals import post_migrate_triggers, pre_migrate_functions


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        pre_migrate.connect(pre_migrate_functions, self)
        post_migrate.connect(post_migrate_triggers, self)
