from django_filters import rest_framework as filter
from .models import Usuario
from empresa.filters import lookup_types


class UsuarioFilter(filter.FilterSet):
    class Meta:
        model = Usuario
        fields = {
            'username': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'first_name': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'last_name': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'email': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'telefone': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'celular': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'observacoes': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
            'media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
            'empresa': ['exact', ],
            'empresa__cpf_cnpj': lookup_types['cpf_cnpj'],
            'empresa__razao_social': lookup_types['razao_social'],
            'empresa__nome_fantasia': lookup_types['nome_fantasia'],
            'empresa__logradouro': lookup_types['logradouro'],
            'empresa__numero': lookup_types['numero'],
            'empresa__complemento': lookup_types['complemento'],
            'empresa__bairro': lookup_types['bairro'],
            'empresa__municipio': lookup_types['municipio'],
            'empresa__uf': lookup_types['uf'],
            'empresa__cep': lookup_types['cep'],
            'empresa__pais': lookup_types['pais'],
            'empresa__telefone': lookup_types['telefone'],
            'empresa__media_avaliacoes': lookup_types['media_avaliacoes'],
            'empresa__prestadora_servico': lookup_types['prestadora_servico'],
            'empresa__ativo': lookup_types['ativo'],
            'last_login': ['exact', ],
            'is_superuser': ['exact', ],
            'is_staff': ['exact', ],
            'is_active': ['exact', ],
            'groups': [],
        }