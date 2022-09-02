from django_filters import rest_framework as filter
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from usuario.filters import lookup_types_usuario
from empresa.filters import lookup_types_empresa

lookup_types_politica_privacidade = {
    'codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'titulo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'tipo_titular': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    'data_validade': [
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
    'ativo': ['exact', ],
    'data_cadastro': [
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
    'hora_cadastro': [
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
}

lookup_types_consentimento_politica_privacidade = {
    'titular': ['exact', ],
    'politica_privacidade': ['exact', ],
    'consentimento': ['exact', ],
    'data_cadastro': [
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
    'hora_cadastro': [
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
}


class PoliticaPrivacidadeFilter(filter.FilterSet):
    class Meta:
        model = PoliticaPrivacidade
        fields = {
            'codigo': lookup_types_politica_privacidade['codigo'],
            'titulo': lookup_types_politica_privacidade['titulo'],
            'descricao': lookup_types_politica_privacidade['descricao'],
            'tipo_titular': lookup_types_politica_privacidade['tipo_titular'],
            'data_validade': lookup_types_politica_privacidade['data_validade'],
            'ativo': lookup_types_politica_privacidade['ativo'],
            'data_cadastro': lookup_types_politica_privacidade['data_cadastro'],
            'hora_cadastro': lookup_types_politica_privacidade['hora_cadastro'],
        }


class ConsentimentoPoliticaPrivacidadeFilter(filter.FilterSet):
    class Meta:
        model = ConsentimentoPoliticaPrivacidade
        fields = {
            'titular': lookup_types_consentimento_politica_privacidade['titular'],
            'titular__username': lookup_types_usuario['username'],
            'titular__first_name': lookup_types_usuario['first_name'],
            'titular__last_name': lookup_types_usuario['last_name'],
            'titular__email': lookup_types_usuario['email'],
            'titular__telefone': lookup_types_usuario['telefone'],
            'titular__celular': lookup_types_usuario['celular'],
            'titular__observacoes': lookup_types_usuario['observacoes'],
            'titular__media_avaliacoes': lookup_types_usuario['media_avaliacoes'],
            'titular__empresa': lookup_types_usuario['empresa'],
            'titular__empresa__cpf_cnpj': lookup_types_empresa['cpf_cnpj'],
            'titular__empresa__razao_social': lookup_types_empresa['razao_social'],
            'titular__empresa__nome_fantasia': lookup_types_empresa['nome_fantasia'],
            'titular__empresa__logradouro': lookup_types_empresa['logradouro'],
            'titular__empresa__numero': lookup_types_empresa['numero'],
            'titular__empresa__complemento': lookup_types_empresa['complemento'],
            'titular__empresa__bairro': lookup_types_empresa['bairro'],
            'titular__empresa__municipio': lookup_types_empresa['municipio'],
            'titular__empresa__uf': lookup_types_empresa['uf'],
            'titular__empresa__cep': lookup_types_empresa['cep'],
            'titular__empresa__pais': lookup_types_empresa['pais'],
            'titular__empresa__telefone': lookup_types_empresa['telefone'],
            'titular__empresa__media_avaliacoes': lookup_types_empresa['media_avaliacoes'],
            'titular__empresa__prestadora_servico': lookup_types_empresa['prestadora_servico'],
            'titular__empresa__ativo': lookup_types_empresa['ativo'],
            'titular__last_login': lookup_types_usuario['last_login'],
            'titular__is_staff': lookup_types_usuario['is_staff'],
            'titular__is_manager': lookup_types_usuario['is_manager'],
            'titular__is_superuser': lookup_types_usuario['is_superuser'],
            'titular__is_active': lookup_types_usuario['is_active'],
            'titular__groups': lookup_types_usuario['groups'],
            'politica_privacidade': lookup_types_consentimento_politica_privacidade['politica_privacidade'],
            'politica_privacidade__codigo': lookup_types_politica_privacidade['codigo'],
            'politica_privacidade__titulo': lookup_types_politica_privacidade['titulo'],
            'politica_privacidade__descricao': lookup_types_politica_privacidade['descricao'],
            'politica_privacidade__tipo_titular': lookup_types_politica_privacidade['tipo_titular'],
            'politica_privacidade__data_validade': lookup_types_politica_privacidade['data_validade'],
            'politica_privacidade__ativo': lookup_types_politica_privacidade['ativo'],
            'politica_privacidade__data_cadastro': lookup_types_politica_privacidade['data_cadastro'],
            'politica_privacidade__hora_cadastro': lookup_types_politica_privacidade['hora_cadastro'],
            'consentimento': lookup_types_consentimento_politica_privacidade['consentimento'],
            'data_cadastro': lookup_types_consentimento_politica_privacidade['data_cadastro'],
            'hora_cadastro': lookup_types_consentimento_politica_privacidade['hora_cadastro'],
        }
