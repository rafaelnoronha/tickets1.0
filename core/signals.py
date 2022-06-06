from django.db import connection
from core.functions import fnc_media_avaliacao_usuario
from ticket.triggers import trg_ticket_prioridade, trg_ticket_status, trg_ticket_atendente, trg_ticket_solucao, \
                            trg_ticket_cancelado, trg_mensagem_ticket_solucao, trg_ticket_avaliacao_solicitante, \
                            trg_ticket_finalizado, trg_ticket_avaliacao_atendente


def post_migrate_triggers(sender, **kwargs):
    with connection.cursor() as cursor:
        """
            FUNCTIONS
        """
        cursor.execute(fnc_media_avaliacao_usuario.function())

        """
            TRIGGERS
        """
        cursor.execute(trg_ticket_prioridade.trigger())
        cursor.execute(trg_ticket_status.trigger())
        cursor.execute(trg_ticket_atendente.trigger())
        cursor.execute(trg_ticket_solucao.trigger())
        cursor.execute(trg_ticket_finalizado.trigger())
        cursor.execute(trg_ticket_cancelado.trigger())
        cursor.execute(trg_ticket_avaliacao_solicitante.trigger())
        cursor.execute(trg_ticket_avaliacao_atendente.trigger())

        cursor.execute(trg_mensagem_ticket_solucao.trigger())
