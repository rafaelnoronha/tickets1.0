from django.db import connection
from core.functions import fnc_media_avaliacao_usuario
from ticket.triggers import trg_ticket_movimento_base, trg_ticket_prioridade, trg_ticket_status, trg_mensagem_ticket_solucao, \
                            trg_ticket_avaliacao_solicitante


def pre_migrate_functions(sender, **kwargs):
    with connection.cursor() as cursor:
        """
            FUNCTIONS
        """
        # cursor.execute(fnc_media_avaliacao_usuario.function())


def post_migrate_triggers(sender, **kwargs):
    with connection.cursor() as cursor:
        """
            TRIGGERS
        """
        # cursor.execute(trg_ticket_prioridade.trigger())
        # cursor.execute(trg_ticket_status.trigger())
        # cursor.execute(trg_ticket_avaliacao_solicitante.trigger())
        # cursor.execute(trg_ticket_movimento_base.trigger())

        # cursor.execute(trg_mensagem_ticket_solucao.trigger())
