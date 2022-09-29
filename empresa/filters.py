from django_filters import rest_framework as filters
from .models import Empresa

def lookup_types_empresa(prefixo=''):
    return {
        f'{prefixo}mp_cpf_cnpj': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_razao_social': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_nome_fantasia': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_logradouro': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_numero': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_complemento': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_bairro': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_municipio': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_uf': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_cep': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_pais': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_telefone': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}mp_media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
        f'{prefixo}mp_prestadora_servico': ['exact', ],
        f'{prefixo}mp_ativo': ['iexact', ],
        f'{prefixo}mp_data_cadastro': [
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
        f'{prefixo}mp_hora_cadastro': [
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
