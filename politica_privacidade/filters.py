from django_filters import rest_framework as filter
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from usuario.filters import lookup_types_usuario, lookup_types_classificacao
from empresa.filters import lookup_types_empresa

def lookup_types_politica_privacidade(prefixo=''):
    return {
        f'{prefixo}pl_codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}pl_titulo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}pl_descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}pl_tipo_titular': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}pl_data_validade': [
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
        f'{prefixo}pl_ativo': ['exact', ],
        f'{prefixo}pl_data_cadastro': [
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
        f'{prefixo}pl_hora_cadastro': [
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

def lookup_types_consentimento_politica_privacidade(prefixo=''):
    return {
        f'{prefixo}cn_titular': ['exact', ],
        f'{prefixo}cn_politica_privacidade': ['exact', ],
        f'{prefixo}cn_consentimento': ['exact', ],
        f'{prefixo}cn_data_cadastro': [
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
        f'{prefixo}cn_hora_cadastro': [
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
        fields = lookup_types_politica_privacidade()


class ConsentimentoPoliticaPrivacidadeFilter(filter.FilterSet):
    class Meta:
        fields_consentimento_politica_privacidade = lookup_types_consentimento_politica_privacidade()
        fields_consentimento_politica_privacidade.update(lookup_types_usuario('cn_titular__'))
        fields_consentimento_politica_privacidade.update(lookup_types_empresa('cn_titular__empresa__'))
        fields_consentimento_politica_privacidade.update(lookup_types_classificacao('cn_titular__classificacao__'))
        fields_consentimento_politica_privacidade.update(lookup_types_politica_privacidade('cn_politica_privacidade__'))

        model = ConsentimentoPoliticaPrivacidade
        fields = fields_consentimento_politica_privacidade
