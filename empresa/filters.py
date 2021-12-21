from django_filters import rest_framework as filters
from .models import Empresa


class EmpresaFilter(filters.FilterSet):
    class Meta:
        model = Empresa
        fields = {
            'cpf_cnpj': ['exact', 'contains'],
            'razao_social': ['icontains',],
            'nome_fantasia': ['icontains',],
            'logradouro': ['icontains',],
            'numero': ['icontains',],
            'complemento': ['icontains',],
            'bairro': ['icontains',],
            'municipio': ['icontains',],
            'uf': ['exact', 'icontains',],
            'cep': ['exact', 'icontains',],
            'pais': ['exact', 'icontains',],
            'telefone': ['exact', 'icontains',],
            'media_avaliacoes': ['exact', 'icontains',],
            'prestadora_servico': ['exact', 'icontains',],
            'ativo': ['exact',],
        }
