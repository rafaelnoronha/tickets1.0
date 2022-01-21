from django_filters import rest_framework as filter
from .models import Usuario, LogAutenticacao
from empresa.filters import lookup_types_empresa

lookup_types_usuario = {
    'username': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'first_name': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'last_name': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'email': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'telefone': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'celular': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'observacoes': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'media_avaliacoes': ['exact', 'contains', 'gt', 'gte', 'lt', 'lte', 'in', 'range'],
    'empresa': ['exact', ],
    'last_login': ['exact', ],
    'is_superuser': ['exact', ],
    'is_staff': ['exact', ],
    'is_active': ['exact', ],
    'groups': [],
}

lookup_types_log_autenticacao = {
    'ip': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'autenticado': ['exact', ],
    'data_autenticacao': [
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
    'hora_autenticacao': [
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
    'usuario': ['exact', ],
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
            'usuario__username': lookup_types_usuario['username'],
            'usuario__first_name': lookup_types_usuario['first_name'],
            'usuario__last_name': lookup_types_usuario['last_name'],
            'usuario__email': lookup_types_usuario['email'],
            'usuario__telefone': lookup_types_usuario['telefone'],
            'usuario__celular': lookup_types_usuario['celular'],
            'usuario__observacoes': lookup_types_usuario['observacoes'],
            'usuario__media_avaliacoes': lookup_types_usuario['media_avaliacoes'],
            'usuario__empresa': lookup_types_usuario['empresa'],
            'usuario__empresa__cpf_cnpj': lookup_types_empresa['cpf_cnpj'],
            'usuario__empresa__razao_social': lookup_types_empresa['razao_social'],
            'usuario__empresa__nome_fantasia': lookup_types_empresa['nome_fantasia'],
            'usuario__empresa__logradouro': lookup_types_empresa['logradouro'],
            'usuario__empresa__numero': lookup_types_empresa['numero'],
            'usuario__empresa__complemento': lookup_types_empresa['complemento'],
            'usuario__empresa__bairro': lookup_types_empresa['bairro'],
            'usuario__empresa__municipio': lookup_types_empresa['municipio'],
            'usuario__empresa__uf': lookup_types_empresa['uf'],
            'usuario__empresa__cep': lookup_types_empresa['cep'],
            'usuario__empresa__pais': lookup_types_empresa['pais'],
            'usuario__empresa__telefone': lookup_types_empresa['telefone'],
            'usuario__empresa__media_avaliacoes': lookup_types_empresa['media_avaliacoes'],
            'usuario__empresa__prestadora_servico': lookup_types_empresa['prestadora_servico'],
            'usuario__empresa__ativo': lookup_types_empresa['ativo'],
            'usuario__last_login': lookup_types_usuario['last_login'],
            'usuario__is_superuser': lookup_types_usuario['is_superuser'],
            'usuario__is_staff': lookup_types_usuario['is_staff'],
            'usuario__is_active': lookup_types_usuario['is_active'],
            'usuario__groups': lookup_types_usuario['groups'],
        }