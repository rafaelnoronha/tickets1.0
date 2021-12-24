from django_filters import rest_framework as filter
from .models import Usuario, LogAutenticacao
from empresa.filters import lookup_types_empresa

lookup_types_usuario = {
    'username': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'first_name': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'last_name': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'email': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'telefone': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'celular': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'observacoes': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
    'empresa': ['exact', ],
    'last_login': ['exact', ],
    'is_superuser': ['exact', ],
    'is_staff': ['exact', ],
    'is_active': ['exact', ],
    'groups': [],
}

lookup_types_log_autenticacao = {
    'ip': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'autenticado': ['exact', ],
    'data_autenticacao': ['range', 'year', 'iso_year', 'month', 'day', ],
    'hora_autenticacao': ['range', ],
    'usuario': [],
}


class UsuarioFilter(filter.FilterSet):
    class Meta:
        model = Usuario
        fields = {
            'username': lookup_types_usuario['username'],
            'first_name': lookup_types_usuario['first_name'],
            'last_name': lookup_types_usuario['last_name'],
            'email': lookup_types_usuario['email'],
            'telefone': lookup_types_usuario['telefone'],
            'celular': lookup_types_usuario['celular'],
            'observacoes': lookup_types_usuario['observacoes'],
            'media_avaliacoes': lookup_types_usuario['media_avaliacoes'],
            'empresa': lookup_types_usuario['empresa'],
            'empresa__cpf_cnpj': lookup_types_empresa['cpf_cnpj'],
            'empresa__razao_social': lookup_types_empresa['razao_social'],
            'empresa__nome_fantasia': lookup_types_empresa['nome_fantasia'],
            'empresa__logradouro': lookup_types_empresa['logradouro'],
            'empresa__numero': lookup_types_empresa['numero'],
            'empresa__complemento': lookup_types_empresa['complemento'],
            'empresa__bairro': lookup_types_empresa['bairro'],
            'empresa__municipio': lookup_types_empresa['municipio'],
            'empresa__uf': lookup_types_empresa['uf'],
            'empresa__cep': lookup_types_empresa['cep'],
            'empresa__pais': lookup_types_empresa['pais'],
            'empresa__telefone': lookup_types_empresa['telefone'],
            'empresa__media_avaliacoes': lookup_types_empresa['media_avaliacoes'],
            'empresa__prestadora_servico': lookup_types_empresa['prestadora_servico'],
            'empresa__ativo': lookup_types_empresa['ativo'],
            'last_login': lookup_types_usuario['last_login'],
            'is_superuser': lookup_types_usuario['is_superuser'],
            'is_staff': lookup_types_usuario['is_staff'],
            'is_active': lookup_types_usuario['is_active'],
            'groups': lookup_types_usuario['groups'],
        }


class LogAutenticacaoFilter(filter.FilterSet):
    class Meta:
        model = LogAutenticacao
        fields = {
            'ip': lookup_types_log_autenticacao['ip'],
            'autenticado': lookup_types_log_autenticacao['autenticado'],
            'data_autenticacao': lookup_types_log_autenticacao['data_autenticacao'],
            'hora_autenticacao': lookup_types_log_autenticacao['hora_autenticacao'],
            'usuario': lookup_types_log_autenticacao['usuario'],
        }