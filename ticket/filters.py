from django_filters import rest_framework as filter
from .models import Ticket, MensagemTicket
from usuario.filters import lookup_types_usuario
from empresa.filters import lookup_types_empresa

lookup_types_ticket = {
    'status': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'solicitante': ['exact', ],
    'atendente': ['exact', ],
    'titulo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', ],
    'avaliacao_solicitante': [
        'exact',
        'iexact',
        'icontains',
        'istartswith',
        'iendswith',
        'in',
        'range',
        'gte',
        'lte',
        'gt',
        'lt',
    ],
    'avaliacao_atendente': [
        'exact',
        'iexact',
        'icontains',
        'istartswith',
        'iendswith',
        'in',
        'range',
        'gte',
        'lte',
        'gt',
        'lt',
    ],
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
}

lookup_types_mensagem_ticket = {

}


class TicketFilter(filter.FilterSet):
    class Meta:
        model = Ticket
        fields = {
            'status': lookup_types_ticket['status'],
            'solicitante': lookup_types_ticket['solicitante'],
            'solicitante__username': lookup_types_usuario['username'],
            'solicitante__first_name': lookup_types_usuario['first_name'],
            'solicitante__last_name': lookup_types_usuario['last_name'],
            'solicitante__email': lookup_types_usuario['email'],
            'solicitante__telefone': lookup_types_usuario['telefone'],
            'solicitante__celular': lookup_types_usuario['celular'],
            'solicitante__observacoes': lookup_types_usuario['observacoes'],
            'solicitante__media_avaliacoes': lookup_types_usuario['media_avaliacoes'],
            'solicitante__empresa': lookup_types_usuario['empresa'],
            'solicitante__empresa__cpf_cnpj': lookup_types_empresa['cpf_cnpj'],
            'solicitante__empresa__razao_social': lookup_types_empresa['razao_social'],
            'solicitante__empresa__nome_fantasia': lookup_types_empresa['nome_fantasia'],
            'solicitante__empresa__logradouro': lookup_types_empresa['logradouro'],
            'solicitante__empresa__numero': lookup_types_empresa['numero'],
            'solicitante__empresa__complemento': lookup_types_empresa['complemento'],
            'solicitante__empresa__bairro': lookup_types_empresa['bairro'],
            'solicitante__empresa__municipio': lookup_types_empresa['municipio'],
            'solicitante__empresa__uf': lookup_types_empresa['uf'],
            'solicitante__empresa__cep': lookup_types_empresa['cep'],
            'solicitante__empresa__pais': lookup_types_empresa['pais'],
            'solicitante__empresa__telefone': lookup_types_empresa['telefone'],
            'solicitante__empresa__media_avaliacoes': lookup_types_empresa['media_avaliacoes'],
            'solicitante__empresa__prestadora_servico': lookup_types_empresa['prestadora_servico'],
            'solicitante__empresa__ativo': lookup_types_empresa['ativo'],
            'solicitante__last_login': lookup_types_usuario['last_login'],
            'solicitante__is_superuser': lookup_types_usuario['is_superuser'],
            'solicitante__is_staff': lookup_types_usuario['is_staff'],
            'solicitante__is_active': lookup_types_usuario['is_active'],
            'solicitante__groups': lookup_types_usuario['groups'],
            'atendente': lookup_types_ticket['atendente'],
            'atendente__username': lookup_types_usuario['username'],
            'atendente__first_name': lookup_types_usuario['first_name'],
            'atendente__last_name': lookup_types_usuario['last_name'],
            'atendente__email': lookup_types_usuario['email'],
            'atendente__telefone': lookup_types_usuario['telefone'],
            'atendente__celular': lookup_types_usuario['celular'],
            'atendente__observacoes': lookup_types_usuario['observacoes'],
            'atendente__media_avaliacoes': lookup_types_usuario['media_avaliacoes'],
            'atendente__empresa': lookup_types_usuario['empresa'],
            'atendente__empresa__cpf_cnpj': lookup_types_empresa['cpf_cnpj'],
            'atendente__empresa__razao_social': lookup_types_empresa['razao_social'],
            'atendente__empresa__nome_fantasia': lookup_types_empresa['nome_fantasia'],
            'atendente__empresa__logradouro': lookup_types_empresa['logradouro'],
            'atendente__empresa__numero': lookup_types_empresa['numero'],
            'atendente__empresa__complemento': lookup_types_empresa['complemento'],
            'atendente__empresa__bairro': lookup_types_empresa['bairro'],
            'atendente__empresa__municipio': lookup_types_empresa['municipio'],
            'atendente__empresa__uf': lookup_types_empresa['uf'],
            'atendente__empresa__cep': lookup_types_empresa['cep'],
            'atendente__empresa__pais': lookup_types_empresa['pais'],
            'atendente__empresa__telefone': lookup_types_empresa['telefone'],
            'atendente__empresa__media_avaliacoes': lookup_types_empresa['media_avaliacoes'],
            'atendente__empresa__prestadora_servico': lookup_types_empresa['prestadora_servico'],
            'atendente__empresa__ativo': lookup_types_empresa['ativo'],
            'atendente__last_login': lookup_types_usuario['last_login'],
            'atendente__is_superuser': lookup_types_usuario['is_superuser'],
            'atendente__is_staff': lookup_types_usuario['is_staff'],
            'atendente__is_active': lookup_types_usuario['is_active'],
            'atendente__groups': lookup_types_usuario['groups'],
            'titulo': lookup_types_ticket['titulo'],
            'descricao': lookup_types_ticket['descricao'],
            'avaliacao_solicitante': lookup_types_ticket['avaliacao_solicitante'],
            'avaliacao_atendente': lookup_types_ticket['avaliacao_atendente'],
            'data_cadastro': lookup_types_ticket['data_cadastro'],
        }


class MensagemTicketFilter(filter.FilterSet):
    class Meta:
        model = MensagemTicket
        fields = {

        }
