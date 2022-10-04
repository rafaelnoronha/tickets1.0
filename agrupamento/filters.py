from django_filters import rest_framework as filter
from .models import Agrupamento, Classificacao

def lookup_types_agrupamento(prefixo=''):
    return {
        f'{prefixo}gr_codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}gr_nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}gr_prioridade': [
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
        f'{prefixo}gr_tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}ativo': ['iexact', ],
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

def lookup_types_classificacao(prefixo=''):
    return {
        f'{prefixo}cl_codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}cl_nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}cl_descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    }


class AgrupamentoFilter(filter.FilterSet):
    class Meta:
        model = Agrupamento
        fields = lookup_types_agrupamento()


class ClassificacaoFilter(filter.FilterSet):
    class Meta:
        model = Classificacao
        fields = lookup_types_classificacao()
