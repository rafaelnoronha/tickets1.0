from django_filters import rest_framework as filter
from .models import Usuario
from empresa.filters import lookup_types_empresa
from agrupamento.filters import lookup_types_classificacao

def lookup_types_usuario(prefixo=''):
    return {
        f'{prefixo}username': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}first_name': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}last_name': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}email': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}telefone': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}celular': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}classificacao': ['exact', ],
        f'{prefixo}observacoes': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
        f'{prefixo}empresa': ['exact', ],
        f'{prefixo}last_login': ['exact', ],
        f'{prefixo}is_staff': ['exact', ],
        f'{prefixo}is_manager': ['exact', ],
        f'{prefixo}is_superuser': ['exact', ],
        f'{prefixo}is_active': ['exact', ],
        f'{prefixo}groups': [],
}


class UsuarioFilter(filter.FilterSet):
    class Meta:
        fields_usuario = lookup_types_usuario()
        fields_usuario.update(lookup_types_classificacao('classificacao__'))
        fields_usuario.update(lookup_types_empresa('empresa__'))

        model = Usuario
        fields = fields_usuario
