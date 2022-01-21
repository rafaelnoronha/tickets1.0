from django_filters import rest_framework as filter
from .models import Auditoria
from usuario.filters import lookup_types_usuario
from empresa.filters import lookup_types_empresa

lookup_types_auditoria = {
    'data_operacao': [
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
    'hora_operacao': [
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
    'tabela_operacao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'tipo_operacao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'usuario_operacao': ['exact', ],
    'estado_anterior': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'estado_atual': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
}


class AuditoriaFilter(filter.FilterSet):
    class Meta:
        model = Auditoria
        fields = {
            'data_operacao': lookup_types_auditoria['data_operacao'],
            'hora_operacao': lookup_types_auditoria['hora_operacao'],
            'tabela_operacao': lookup_types_auditoria['tabela_operacao'],
            'tipo_operacao': lookup_types_auditoria['tipo_operacao'],
            'usuario_operacao': lookup_types_auditoria['usuario_operacao'],
            'usuario_operacao__username': lookup_types_usuario['username'],
            'usuario_operacao__first_name': lookup_types_usuario['first_name'],
            'usuario_operacao__last_name': lookup_types_usuario['last_name'],
            'usuario_operacao__email': lookup_types_usuario['email'],
            'usuario_operacao__telefone': lookup_types_usuario['telefone'],
            'usuario_operacao__celular': lookup_types_usuario['celular'],
            'usuario_operacao__observacoes': lookup_types_usuario['observacoes'],
            'usuario_operacao__media_avaliacoes': lookup_types_usuario['media_avaliacoes'],
            'usuario_operacao__empresa': lookup_types_usuario['empresa'],
            'usuario_operacao__empresa__cpf_cnpj': lookup_types_empresa['cpf_cnpj'],
            'usuario_operacao__empresa__razao_social': lookup_types_empresa['razao_social'],
            'usuario_operacao__empresa__nome_fantasia': lookup_types_empresa['nome_fantasia'],
            'usuario_operacao__empresa__logradouro': lookup_types_empresa['logradouro'],
            'usuario_operacao__empresa__numero': lookup_types_empresa['numero'],
            'usuario_operacao__empresa__complemento': lookup_types_empresa['complemento'],
            'usuario_operacao__empresa__bairro': lookup_types_empresa['bairro'],
            'usuario_operacao__empresa__municipio': lookup_types_empresa['municipio'],
            'usuario_operacao__empresa__uf': lookup_types_empresa['uf'],
            'usuario_operacao__empresa__cep': lookup_types_empresa['cep'],
            'usuario_operacao__empresa__pais': lookup_types_empresa['pais'],
            'usuario_operacao__empresa__telefone': lookup_types_empresa['telefone'],
            'usuario_operacao__empresa__media_avaliacoes': lookup_types_empresa['media_avaliacoes'],
            'usuario_operacao__empresa__prestadora_servico': lookup_types_empresa['prestadora_servico'],
            'usuario_operacao__empresa__ativo': lookup_types_empresa['ativo'],
            'usuario_operacao__last_login': lookup_types_usuario['last_login'],
            'usuario_operacao__is_superuser': lookup_types_usuario['is_superuser'],
            'usuario_operacao__is_staff': lookup_types_usuario['is_staff'],
            'usuario_operacao__is_active': lookup_types_usuario['is_active'],
            'usuario_operacao__groups': lookup_types_usuario['groups'],
            'estado_anterior': lookup_types_auditoria['estado_anterior'],
            'estado_atual': lookup_types_auditoria['estado_atual'],
        }
