from django_filters import rest_framework as filters
from .models import Empresa


class EmpresaFilter(filters.FilterSet):
    class Meta:
        model = Empresa
        fields = {
            'cpf_cnpj': ['exact', 'iexact', 'icontains', 'in', ],
            'razao_social': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'nome_fantasia': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'logradouro': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'numero': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'complemento': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'bairro': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'municipio': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'uf': ['exact', 'iexact', 'icontains', 'in', ],
            'cep': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'pais': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'telefone': ['exact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
            'prestadora_servico': ['exact', 'in', ],
            'ativo': ['iexact', ],
        }
