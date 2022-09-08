from django_filters import rest_framework as filter
from .models import Auditoria
from usuario.filters import lookup_types_classificacao, lookup_types_usuario
from empresa.filters import lookup_types_empresa

def lookup_types_auditoria(prefixo=''):
    return {
        f'{prefixo}data_operacao': [
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
        f'{prefixo}hora_operacao': [
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
        f'{prefixo}tabela_operacao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}tipo_operacao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}usuario_operacao': ['exact', ],
        f'{prefixo}estado_anterior': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}estado_atual': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
    }


class AuditoriaFilter(filter.FilterSet):
    class Meta:
        fields_auditoria = lookup_types_auditoria()
        fields_auditoria.update(lookup_types_usuario('usuario_operacao__'))
        fields_auditoria.update(lookup_types_empresa('usuario_operacao__empresa__'))
        fields_auditoria.update(lookup_types_classificacao('usuario_operacao__classificacao__'))

        model = Auditoria
        fields = fields_auditoria
