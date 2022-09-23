from django_filters import rest_framework as filter
from .models import Ticket, MensagemTicket, MovimentoTicket
from usuario.filters import lookup_types_usuario, lookup_types_classificacao
from empresa.filters import lookup_types_empresa
from agrupamento.filters import lookup_types_agrupamento

def lookup_types_ticket(prefixo=''):
    return {
        f'{prefixo}status': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}solicitante': ['exact', ],
        f'{prefixo}classificacao_atendente': ['exact', ],
        f'{prefixo}atendente': ['exact', ],
        f'{prefixo}titulo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}grupo': ['exact', ],
        f'{prefixo}subgrupo': ['exact', ],
        f'{prefixo}avaliacao_solicitante': [
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
        f'{prefixo}observacao_avaliacao_solicitante': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
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
        'usuario': ['exact', ],
        'ticket': ['exact', ],
        'mensagem': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        'mensagem_relacionada': ['exact', ],
        'solucao': ['iexact', ],
        'data_cadastro': [
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
        'hora_cadastro': [
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
        f'{prefixo}ticket': ['exact', ],
        f'{prefixo}data_inicio': [
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
        f'{prefixo}hora_inicio': [
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
        f'{prefixo}data_fim': [
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
        f'{prefixo}hora_fim': [
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
        f'{prefixo}classificacao_atendente': ['exact', ],
        f'{prefixo}atendente': ['exact', ],
        f'{prefixo}solucao': ['exact', ],
        f'{prefixo}finalizado': ['exact', ],
        f'{prefixo}cancelado': ['exact', ],
        f'{prefixo}motivo_cancelamento': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
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
        
        fields_ticket.update(lookup_types_usuario('solicitante__'))
        fields_ticket.update(lookup_types_empresa('solicitante__empresa__'))
        fields_ticket.update(lookup_types_classificacao('solicitante__classificacao__'))

        fields_ticket.update(lookup_types_usuario('atendente__'))
        fields_ticket.update(lookup_types_empresa('atendente__empresa__'))
        fields_ticket.update(lookup_types_classificacao('atendente__classificacao__'))

        fields_ticket.update(lookup_types_classificacao('classificacao_atendente__'))

        fields_ticket.update(lookup_types_agrupamento('grupo__'))
        fields_ticket.update(lookup_types_agrupamento('subgrupo__'))

        model = Ticket
        fields = fields_ticket


class MensagemTicketFilter(filter.FilterSet):
    class Meta:
        fields_mensagem_ticket = lookup_types_mensagem_ticket()

        fields_mensagem_ticket.update(lookup_types_usuario('usuario__'))
        fields_mensagem_ticket.update(lookup_types_empresa('usuario__empresa__'))
        fields_mensagem_ticket.update(lookup_types_classificacao('usuario__classificacao__'))

        fields_mensagem_ticket.update(lookup_types_ticket('ticket__'))
        fields_mensagem_ticket.update(lookup_types_usuario('ticket__solicitante__'))
        fields_mensagem_ticket.update(lookup_types_empresa('ticket__solicitante__empresa__'))
        fields_mensagem_ticket.update(lookup_types_classificacao('ticket__solicitante__classificacao__'))

        fields_mensagem_ticket.update(lookup_types_usuario('ticket__atendente__'))
        fields_mensagem_ticket.update(lookup_types_empresa('ticket__atendente__empresa__'))
        fields_mensagem_ticket.update(lookup_types_classificacao('ticket__atendente__classificacao__'))

        fields_mensagem_ticket.update(lookup_types_classificacao('ticket__classificacao_atendente__'))

        fields_mensagem_ticket.update(lookup_types_agrupamento('ticket__grupo__'))
        fields_mensagem_ticket.update(lookup_types_agrupamento('ticket__subgrupo__'))

        model = MensagemTicket
        fields = fields_mensagem_ticket


class MovimentoTicketFilter(filter.FilterSet):
    class Meta:
        fields_movimento_ticket = lookup_types_movimento_ticket()

        fields_movimento_ticket.update(lookup_types_ticket('ticket__'))
        fields_movimento_ticket.update(lookup_types_usuario('ticket__solicitante__'))
        fields_movimento_ticket.update(lookup_types_empresa('ticket__solicitante__empresa__'))
        fields_movimento_ticket.update(lookup_types_classificacao('ticket__solicitante__classificacao__'))

        fields_movimento_ticket.update(lookup_types_usuario('ticket__atendente__'))
        fields_movimento_ticket.update(lookup_types_empresa('ticket__atendente__empresa__'))
        fields_movimento_ticket.update(lookup_types_classificacao('ticket__atendente__classificacao__'))

        fields_movimento_ticket.update(lookup_types_classificacao('ticket__classificacao_atendente__'))

        fields_movimento_ticket.update(lookup_types_agrupamento('ticket__grupo__'))
        fields_movimento_ticket.update(lookup_types_agrupamento('ticket__subgrupo__'))
        
        fields_movimento_ticket.update(lookup_types_ticket('solucao__ticket__'))
        fields_movimento_ticket.update(lookup_types_usuario('solucao__usuario__'))
        fields_movimento_ticket.update(lookup_types_empresa('solucao__usuario__empresa__'))
        fields_movimento_ticket.update(lookup_types_classificacao('solucao__usuario__classificacao__'))

        fields_movimento_ticket.update(lookup_types_usuario('finalizado__'))
        fields_movimento_ticket.update(lookup_types_empresa('finalizado__empresa__'))
        fields_movimento_ticket.update(lookup_types_classificacao('finalizado__classificacao__'))

        fields_movimento_ticket.update(lookup_types_usuario('cancelado__'))
        fields_movimento_ticket.update(lookup_types_empresa('cancelado__empresa__'))
        fields_movimento_ticket.update(lookup_types_classificacao('cancelado__classificacao__'))

        fields_movimento_ticket.update(lookup_types_classificacao('classificacao_atendente__'))

        fields_movimento_ticket.update(lookup_types_usuario('atendente__'))
        fields_movimento_ticket.update(lookup_types_empresa('atendente__empresa__'))
        fields_movimento_ticket.update(lookup_types_classificacao('atendente__classificacao__'))

        model = MovimentoTicket
        fields = fields_movimento_ticket
