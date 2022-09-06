from django_filters import rest_framework as filter
from .models import Grupo, Subgrupo

def lookup_types_grupo(prefixo=''):
    return {
        f'{prefixo}codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}prioridade': [
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
        f'{prefixo}tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
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

def lookup_types_subgrupo(prefixo=''):
    return {
        f'{prefixo}codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}prioridade': [
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
        f'{prefixo}tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
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


class GrupoFilter(filter.FilterSet):
    class Meta:
        model = Grupo
        fields = lookup_types_grupo()


class SubgrupoFilter(filter.FilterSet):
    class Meta:
        model = Subgrupo
        fields = lookup_types_subgrupo()
