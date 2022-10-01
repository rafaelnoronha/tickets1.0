from django_filters import rest_framework as filter
from .models import Auditoria, LogAutenticacao
from usuario.filters import lookup_types_usuario
from agrupamento.filters import lookup_types_classificacao
from empresa.filters import lookup_types_empresa

def lookup_types_auditoria(prefixo=''):
    return {
        f'{prefixo}dt_data_operacao': [
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
        f'{prefixo}dt_hora_operacao': [
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
        f'{prefixo}dt_tabela_operacao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}dt_tipo_operacao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}dt_usuario_operacao': ['exact', ],
        f'{prefixo}dt_estado_anterior': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}dt_estado_atual': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    }

def lookup_types_log_autenticacao(prefixo=''):
    return {
        f'{prefixo}ip': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}autenticado': ['exact', ],
        f'{prefixo}data_autenticacao': [
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
        f'{prefixo}hora_autenticacao': [
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
        f'{prefixo}usuario': ['exact', ],
    }


class AuditoriaFilter(filter.FilterSet):
    class Meta:
        fields_auditoria = lookup_types_auditoria()
        fields_auditoria.update(lookup_types_usuario('dt_usuario_operacao__'))
        fields_auditoria.update(lookup_types_empresa('dt_usuario_operacao__empresa__'))
        fields_auditoria.update(lookup_types_classificacao('dt_usuario_operacao__classificacao__'))

        model = Auditoria
        fields = fields_auditoria


class LogAutenticacaoFilter(filter.FilterSet):
    class Meta:
        fields_log_autenticacao = lookup_types_log_autenticacao()
        fields_log_autenticacao.update(lookup_types_usuario('usuario__'))
        fields_log_autenticacao.update(lookup_types_empresa('usuario__empresa__'))
        fields_log_autenticacao.update(lookup_types_classificacao('usuario__classificacao__'))

        model = LogAutenticacao
        fields = fields_log_autenticacao
