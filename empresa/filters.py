from django_filters import rest_framework as filters
from .models import Empresa

def lookup_types_empresa(prefixo=''):
    return {
        f'{prefixo}cpf_cnpj': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}razao_social': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}nome_fantasia': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}logradouro': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}numero': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}complemento': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}bairro': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}municipio': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}uf': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}cep': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}pais': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}telefone': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
        f'{prefixo}prestadora_servico': ['exact', ],
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


class EmpresaFilter(filters.FilterSet):
    class Meta:
        model = Empresa
        fields = lookup_types_empresa()
