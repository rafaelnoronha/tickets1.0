from django_filters import rest_framework as filter
from .models import Usuario, Classificacao, LogAutenticacao
from empresa.filters import lookup_types_empresa

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

def lookup_types_classificacao(prefixo=''):
    return {
        f'{prefixo}codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}nome': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        f'{prefixo}descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
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


class UsuarioFilter(filter.FilterSet):
    class Meta:
        fields_usuario = lookup_types_usuario()
        fields_usuario.update(lookup_types_classificacao('classificacao__'))
        fields_usuario.update(lookup_types_empresa('empresa__'))

        model = Usuario
        fields = fields_usuario


class ClassificacaoFilter(filter.FilterSet):
    class Meta:
        model = Classificacao
        fields = lookup_types_classificacao()


class LogAutenticacaoFilter(filter.FilterSet):
    class Meta:
        fields_log_autenticacao = lookup_types_log_autenticacao()
        fields_log_autenticacao.update(lookup_types_usuario('usuario__'))
        fields_log_autenticacao.update(lookup_types_empresa('usuario__empresa__'))
        fields_log_autenticacao.update(lookup_types_classificacao('usuario__classificacao__'))

        model = LogAutenticacao
        fields = fields_log_autenticacao
