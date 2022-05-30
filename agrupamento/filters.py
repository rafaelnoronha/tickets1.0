from django_filters import rest_framework as filter
from .models import Grupo, Subgrupo

lookup_types_grupo = {
    'uuid': ['exact', 'in', ],
    'codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'prioridade': [
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
    'tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
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

lookup_types_subgrupo = {
    'uuid': ['exact', 'in', ],
    'codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'prioridade': [
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
    'tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
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


class GrupoFilter(filter.FilterSet):
    class Meta:
        model = Grupo
        fields = {
            'uuid': lookup_types_grupo['uuid'],
            'codigo': lookup_types_grupo['codigo'],
            'nome': lookup_types_grupo['nome'],
            'prioridade': lookup_types_grupo['prioridade'],
            'tipo': lookup_types_grupo['tipo'],
            'data_cadastro': lookup_types_grupo['data_cadastro'],
            'hora_cadastro': lookup_types_grupo['hora_cadastro'],
        }


class SubgrupoFilter(filter.FilterSet):
    class Meta:
        model = Subgrupo
        fields = {
            'uuid': lookup_types_subgrupo['uuid'],
            'codigo': lookup_types_grupo['codigo'],
            'nome': lookup_types_subgrupo['nome'],
            'prioridade': lookup_types_subgrupo['prioridade'],
            'tipo': lookup_types_grupo['tipo'],
            'data_cadastro': lookup_types_subgrupo['data_cadastro'],
        }
