from django_filters import rest_framework as filters
from .models import Empresa


class EmpresaFilter(filters.FilterSet):
    class Meta:
        model = Empresa
        fields = {
            'cpf_cnpj': ['exact', 'iexact', 'icontains'],
            'razao_social': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', ],
            'nome_fantasia': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', ],
            'logradouro': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', ],
            'numero': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', ],
            'complemento': ['exact', 'icontains', 'istartswith', 'iendswith', ],
            'bairro': ['exact', 'icontains', 'istartswith', 'iendswith', ],
            'municipio': ['exact', 'icontains', 'istartswith', 'iendswith', ],
            'uf': ['exact', 'iexact', 'icontains', ],
            'cep': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', ],
            'pais': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', ],
            'telefone': ['exact', 'icontains', 'istartswith', 'iendswith', ],
            'media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', ],
            'prestadora_servico': ['exact', ],
            'ativo': ['iexact', ],
        }
