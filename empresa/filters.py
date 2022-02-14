from django_filters import rest_framework as filters
from .models import Empresa

lookup_types_empresa = {
    'uuid': ['exact', 'in', ],
    'cpf_cnpj': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'razao_social': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'nome_fantasia': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'logradouro': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'numero': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'complemento': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'bairro': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'municipio': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'uf': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'cep': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'pais': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'telefone': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
    'prestadora_servico': ['exact', ],
    'ativo': ['iexact', ],
}


class EmpresaFilter(filters.FilterSet):
    class Meta:
        model = Empresa
        fields = {
            'uuid': lookup_types_empresa['uuid'],
            'cpf_cnpj': lookup_types_empresa['cpf_cnpj'],
            'razao_social': lookup_types_empresa['razao_social'],
            'nome_fantasia': lookup_types_empresa['nome_fantasia'],
            'logradouro': lookup_types_empresa['logradouro'],
            'numero': lookup_types_empresa['numero'],
            'complemento': lookup_types_empresa['complemento'],
            'bairro': lookup_types_empresa['bairro'],
            'municipio': lookup_types_empresa['municipio'],
            'uf': lookup_types_empresa['uf'],
            'cep': lookup_types_empresa['cep'],
            'pais': lookup_types_empresa['pais'],
            'telefone': lookup_types_empresa['telefone'],
            'media_avaliacoes': lookup_types_empresa['media_avaliacoes'],
            'prestadora_servico': lookup_types_empresa['prestadora_servico'],
            'ativo': lookup_types_empresa['ativo'],
        }
