from django_filters import rest_framework as filter
from .models import Grupo, Subgrupo

lookup_types_grupo = {
    'uuid': ['exact', 'in', ],
    'codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'peso': [
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
}

lookup_types_subgrupo = {
    'uuid': ['exact', 'in', ],
    'codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'peso': [
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
}


class GrupoFilter(filter.FilterSet):
    class Meta:
        model = Grupo
        fields = {
            'uuid': lookup_types_grupo['uuid'],
            'codigo': lookup_types_grupo['codigo'],
            'nome': lookup_types_grupo['nome'],
            'peso': lookup_types_grupo['peso'],
            'tipo': lookup_types_grupo['peso'],
        }


class SubgrupoFilter(filter.FilterSet):
    class Meta:
        model = Subgrupo
        fields = {
            'uuid': lookup_types_subgrupo['uuid'],
            'codigo': lookup_types_grupo['codigo'],
            'nome': lookup_types_subgrupo['nome'],
            'peso': lookup_types_subgrupo['peso'],
            'tipo': lookup_types_grupo['peso'],
        }
