from django_filters import rest_framework as filter
from .models import Grupo, Subgrupo

lookup_types_grupo = {
    'uuid': ['exact', 'in', ],
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
}

lookup_types_subgrupo = {
    'uuid': ['exact', 'in', ],
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
}


class GrupoFilter(filter.FilterSet):
    class Meta:
        model = Grupo
        fields = {
            'uuid': lookup_types_grupo['uuid'],
            'nome': lookup_types_grupo['nome'],
            'peso': lookup_types_grupo['peso'],
        }


class SubgrupoFilter(filter.FilterSet):
    class Meta:
        model = Grupo
        fields = {
            'uuid': lookup_types_subgrupo['uuid'],
            'nome': lookup_types_subgrupo['nome'],
            'peso': lookup_types_subgrupo['peso'],
        }
