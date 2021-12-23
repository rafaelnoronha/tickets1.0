from django_filters import rest_framework as filters
from .models import Empresa

lookup_types = {
    'cpf_cnpj': ['exact', 'iexact', 'icontains', 'in', ],
    'razao_social': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'nome_fantasia': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'logradouro': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'numero': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'complemento': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'bairro': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'municipio': ['exact', 'icontains', 'istartswith', 'iendswith', 'in'],
    'uf': ['exact', 'iexact', 'icontains', 'in', ],
    'cep': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'pais': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'telefone': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
    'prestadora_servico': ['exact', 'in', ],
    'ativo': ['iexact', ],
}


class EmpresaFilter(filters.FilterSet):
    class Meta:
        model = Empresa
        fields = {
            'cpf_cnpj': lookup_types['cpf_cnpj'],
            'razao_social': lookup_types['razao_social'],
            'nome_fantasia': lookup_types['nome_fantasia'],
            'logradouro': lookup_types['logradouro'],
            'numero': lookup_types['numero'],
            'complemento': lookup_types['complemento'],
            'bairro': lookup_types['bairro'],
            'municipio': lookup_types['municipio'],
            'uf': lookup_types['uf'],
            'cep': lookup_types['cep'],
            'pais': lookup_types['pais'],
            'telefone': lookup_types['telefone'],
            'media_avaliacoes': lookup_types['media_avaliacoes'],
            'prestadora_servico': lookup_types['prestadora_servico'],
            'ativo': lookup_types['ativo'],
        }
