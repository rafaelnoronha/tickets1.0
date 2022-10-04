from django_filters import rest_framework as filter
from .models import Ticket, MensagemTicket, MovimentoTicket
from usuario.filters import lookup_types_usuario
from agrupamento.filters import lookup_types_classificacao
from empresa.filters import lookup_types_empresa
from agrupamento.filters import lookup_types_agrupamento

def lookup_types_ticket(prefixo=''):
    return {
        f'{prefixo}tc_status': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}tc_solicitante': ['exact', ],
        f'{prefixo}tc_classificacao_atendente': ['exact', ],
        f'{prefixo}tc_atendente': ['exact', ],
        f'{prefixo}tc_titulo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}tc_descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}tc_grupo': ['exact', ],
        f'{prefixo}tc_subgrupo': ['exact', ],
        f'{prefixo}tc_avaliacao_solicitante': [
            'exact',
            'iexact',
            'icontains',
            'istartswith',
            'iendswith',
            'in',
            'range',
            'gte',
            'lte',
            'gt',
            'lt',
        ],
        f'{prefixo}tc_observacao_avaliacao_solicitante': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}ativo': ['exact', ],
        f'{prefixo}data_cadastro': [
            'exact',
            'range',
            'year', 'year__gte', 'year__gt', 'year__lte', 'year__lt', 'year__range', 'year__in',
            'month', 'month__gte', 'month__gt', 'month__lte', 'month__lt', 'month__range', 'month__in',
            'day', 'day__gte', 'day__gt', 'day__lte', 'day__lt', 'day__range', 'day__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
        f'{prefixo}hora_cadastro': [
            'exact',
            'range',
            'hour', 'hour__gte', 'hour__gt', 'hour__lte', 'hour__lt', 'hour__range', 'hour__in',
            'minute', 'minute__gte', 'minute__gt', 'minute__lte', 'minute__lt', 'minute__range', 'minute__in',
            'second', 'second__gte', 'second__gt', 'second__lte', 'second__lt', 'second__range', 'second__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
    }

def lookup_types_mensagem_ticket(prefixo=''):
    return {
        f'{prefixo}mn_usuario': ['exact', ],
        f'{prefixo}mn_ticket': ['exact', ],
        f'{prefixo}mn_mensagem': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mn_mensagem_relacionada': ['exact', ],
        f'{prefixo}mn_solucao': ['iexact', ],
        f'{prefixo}ativo': ['exact', ],
        f'{prefixo}data_cadastro': [
            'exact',
            'range',
            'year', 'year__gte', 'year__gt', 'year__lte', 'year__lt', 'year__range', 'year__in',
            'month', 'month__gte', 'month__gt', 'month__lte', 'month__lt', 'month__range', 'month__in',
            'day', 'day__gte', 'day__gt', 'day__lte', 'day__lt', 'day__range', 'day__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
        f'{prefixo}hora_cadastro': [
            'exact',
            'range',
            'hour', 'hour__gte', 'hour__gt', 'hour__lte', 'hour__lt', 'hour__range', 'hour__in',
            'minute', 'minute__gte', 'minute__gt', 'minute__lte', 'minute__lt', 'minute__range', 'minute__in',
            'second', 'second__gte', 'second__gt', 'second__lte', 'second__lt', 'second__range', 'second__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
    }

def lookup_types_movimento_ticket(prefixo=''):
    return {
        f'{prefixo}mv_ticket': ['exact', ],
        f'{prefixo}mv_data_inicio': [
            'exact',
            'range',
            'year', 'year__gte', 'year__gt', 'year__lte', 'year__lt', 'year__range', 'year__in',
            'month', 'month__gte', 'month__gt', 'month__lte', 'month__lt', 'month__range', 'month__in',
            'day', 'day__gte', 'day__gt', 'day__lte', 'day__lt', 'day__range', 'day__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
        f'{prefixo}mv_hora_inicio': [
            'exact',
            'range',
            'hour', 'hour__gte', 'hour__gt', 'hour__lte', 'hour__lt', 'hour__range', 'hour__in',
            'minute', 'minute__gte', 'minute__gt', 'minute__lte', 'minute__lt', 'minute__range', 'minute__in',
            'second', 'second__gte', 'second__gt', 'second__lte', 'second__lt', 'second__range', 'second__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
        f'{prefixo}mv_data_fim': [
            'exact',
            'range',
            'year', 'year__gte', 'year__gt', 'year__lte', 'year__lt', 'year__range', 'year__in',
            'month', 'month__gte', 'month__gt', 'month__lte', 'month__lt', 'month__range', 'month__in',
            'day', 'day__gte', 'day__gt', 'day__lte', 'day__lt', 'day__range', 'day__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
        f'{prefixo}mv_hora_fim': [
            'exact',
            'range',
            'hour', 'hour__gte', 'hour__gt', 'hour__lte', 'hour__lt', 'hour__range', 'hour__in',
            'minute', 'minute__gte', 'minute__gt', 'minute__lte', 'minute__lt', 'minute__range', 'minute__in',
            'second', 'second__gte', 'second__gt', 'second__lte', 'second__lt', 'second__range', 'second__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
        f'{prefixo}mv_classificacao_atendente': ['exact', ],
        f'{prefixo}mv_atendente': ['exact', ],
        f'{prefixo}mv_solucao': ['exact', ],
        f'{prefixo}mv_finalizado': ['exact', ],
        f'{prefixo}mv_cancelado': ['exact', ],
        f'{prefixo}mv_motivo_cancelamento': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}ativo': ['exact', ],
        f'{prefixo}data_cadastro': [
            'exact',
            'range',
            'year', 'year__gte', 'year__gt', 'year__lte', 'year__lt', 'year__range', 'year__in',
            'month', 'month__gte', 'month__gt', 'month__lte', 'month__lt', 'month__range', 'month__in',
            'day', 'day__gte', 'day__gt', 'day__lte', 'day__lt', 'day__range', 'day__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
        f'{prefixo}hora_cadastro': [
            'exact',
            'range',
            'hour', 'hour__gte', 'hour__gt', 'hour__lte', 'hour__lt', 'hour__range', 'hour__in',
            'minute', 'minute__gte', 'minute__gt', 'minute__lte', 'minute__lt', 'minute__range', 'minute__in',
            'second', 'second__gte', 'second__gt', 'second__lte', 'second__lt', 'second__range', 'second__in',
            'gte',
            'gt',
            'lte',
            'lt',
            'in',
        ],
    }


class TicketFilter(filter.FilterSet):
    class Meta:
        fields_ticket = lookup_types_ticket()
        
        # fields_ticket.update(lookup_types_usuario('tc_solicitante__'))
        # fields_ticket.update(lookup_types_empresa('tc_solicitante__empresa__'))
        # fields_ticket.update(lookup_types_classificacao('tc_solicitante__classificacao__'))

        # fields_ticket.update(lookup_types_usuario('tc_atendente__'))
        # fields_ticket.update(lookup_types_empresa('tc_atendente__empresa__'))
        # fields_ticket.update(lookup_types_classificacao('tc_atendente__classificacao__'))

        # fields_ticket.update(lookup_types_classificacao('tc_classificacao_atendente__'))

        # fields_ticket.update(lookup_types_agrupamento('tc_grupo__'))
        # fields_ticket.update(lookup_types_agrupamento('tc_subgrupo__'))

        model = Ticket
        fields = fields_ticket


class MensagemTicketFilter(filter.FilterSet):
    class Meta:
        fields_mensagem_ticket = lookup_types_mensagem_ticket()

        # fields_mensagem_ticket.update(lookup_types_usuario('mn_usuario__'))
        # fields_mensagem_ticket.update(lookup_types_empresa('mn_usuario__empresa__'))
        # fields_mensagem_ticket.update(lookup_types_classificacao('mn_usuario__classificacao__'))

        # fields_mensagem_ticket.update(lookup_types_ticket('mn_ticket__'))
        # fields_mensagem_ticket.update(lookup_types_usuario('mn_ticket__solicitante__'))
        # fields_mensagem_ticket.update(lookup_types_empresa('mn_ticket__solicitante__empresa__'))
        # fields_mensagem_ticket.update(lookup_types_classificacao('mn_ticket__solicitante__classificacao__'))

        # fields_mensagem_ticket.update(lookup_types_usuario('mn_ticket__atendente__'))
        # fields_mensagem_ticket.update(lookup_types_empresa('mn_ticket__atendente__empresa__'))
        # fields_mensagem_ticket.update(lookup_types_classificacao('mn_ticket__atendente__classificacao__'))

        # fields_mensagem_ticket.update(lookup_types_classificacao('mn_ticket__classificacao_atendente__'))

        # fields_mensagem_ticket.update(lookup_types_agrupamento('mn_ticket__grupo__'))
        # fields_mensagem_ticket.update(lookup_types_agrupamento('mn_ticket__subgrupo__'))

        model = MensagemTicket
        fields = fields_mensagem_ticket


class MovimentoTicketFilter(filter.FilterSet):
    class Meta:
        fields_movimento_ticket = lookup_types_movimento_ticket()

        # fields_movimento_ticket.update(lookup_types_ticket('mv_ticket__'))
        # fields_movimento_ticket.update(lookup_types_usuario('mv_ticket__solicitante__'))
        # fields_movimento_ticket.update(lookup_types_empresa('mv_ticket__solicitante__empresa__'))
        # fields_movimento_ticket.update(lookup_types_classificacao('mv_ticket__solicitante__classificacao__'))

        # fields_movimento_ticket.update(lookup_types_usuario('mv_ticket__atendente__'))
        # fields_movimento_ticket.update(lookup_types_empresa('mv_ticket__atendente__empresa__'))
        # fields_movimento_ticket.update(lookup_types_classificacao('mv_ticket__atendente__classificacao__'))

        # fields_movimento_ticket.update(lookup_types_classificacao('mv_ticket__classificacao_atendente__'))

        # fields_movimento_ticket.update(lookup_types_agrupamento('mv_ticket__grupo__'))
        # fields_movimento_ticket.update(lookup_types_agrupamento('mv_ticket__subgrupo__'))
        
        # fields_movimento_ticket.update(lookup_types_ticket('mv_solucao__ticket__'))
        # fields_movimento_ticket.update(lookup_types_usuario('mv_solucao__usuario__'))
        # fields_movimento_ticket.update(lookup_types_empresa('mv_solucao__usuario__empresa__'))
        # fields_movimento_ticket.update(lookup_types_classificacao('mv_solucao__usuario__classificacao__'))

        # fields_movimento_ticket.update(lookup_types_usuario('mv_finalizado__'))
        # fields_movimento_ticket.update(lookup_types_empresa('mv_finalizado__empresa__'))
        # fields_movimento_ticket.update(lookup_types_classificacao('mv_finalizado__classificacao__'))

        # fields_movimento_ticket.update(lookup_types_usuario('mv_cancelado__'))
        # fields_movimento_ticket.update(lookup_types_empresa('mv_cancelado__empresa__'))
        # fields_movimento_ticket.update(lookup_types_classificacao('mv_cancelado__classificacao__'))

        # fields_movimento_ticket.update(lookup_types_classificacao('mv_classificacao_atendente__'))

        # fields_movimento_ticket.update(lookup_types_usuario('mv_atendente__'))
        # fields_movimento_ticket.update(lookup_types_empresa('mv_atendente__empresa__'))
        # fields_movimento_ticket.update(lookup_types_classificacao('mv_atendente__classificacao__'))

        model = MovimentoTicket
        fields = fields_movimento_ticket
