from rest_framework import serializers
from .models import Ticket, MensagemTicket
from usuario.serializer import UsuarioSerializerSimples
from usuario.models import Usuario
from agrupamento.models import Grupo, Subgrupo
from agrupamento.serializer import GrupoSerializer, SubgrupoSerializer


class TicketSerializerAuditoria(serializers.ModelSerializer):
    solicitante = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    atendente = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    grupo = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    subgrupo = serializers.SlugRelatedField(read_only=True, slug_field='uuid')

    class Meta:
        model = Ticket
        fields = '__all__'


class MensagemTicketSerializerAuditoria(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    mensagem_relacionada = serializers.SlugRelatedField(read_only=True, slug_field='uuid')

    class Meta:
        model = MensagemTicket
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    solicitante = serializers.SlugRelatedField(read_only=True, slug_field='username')
    atendente = serializers.SlugRelatedField(read_only=True, slug_field='username')
    grupo = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    subgrupo = serializers.SlugRelatedField(read_only=True, slug_field='nome')

    class Meta:
        model = Ticket
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'uuid',
            'status',
            'solicitante',
            'atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'avaliacao_atendente',
            'observacao_avaliacao_atendente',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerCreate(TicketSerializer):
    solicitante = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid')
    atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid', allow_null=True)
    grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field='uuid', allow_null=True)
    subgrupo = serializers.SlugRelatedField(queryset=Subgrupo.objects.all(), slug_field='uuid', allow_null=True)

    class Meta:
        model = Ticket
        read_only_fields = [
            'uuid',
        ]
        extra_kwargs = {
            'grupo': {'allow_null': False, 'allow_blank': False},
            'subgrupo': {'allow_null': False, 'allow_blank': False},
        }
        fields = [
            'solicitante',
            'atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
        ]


class TicketSerializerPutPatch(TicketSerializer):
    atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid')
    grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field='uuid', allow_null=True)
    subgrupo = serializers.SlugRelatedField(queryset=Subgrupo.objects.all(), slug_field='uuid', allow_null=True)

    class Meta:
        model = Ticket
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'avaliacao_atendente',
            'observacao_avaliacao_atendente',
            'atendente',
            'grupo',
            'subgrupo',
        ]


class MensagemTicketSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(read_only=True, slug_field='username')
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    mensagem_relacionada = serializers.SlugRelatedField(read_only=True, slug_field='uuid')

    class Meta:
        model = MensagemTicket
        read_only_fields = [
            'uuid',
            'data_cadastro',
            'hora_cadastro',
        ]
        fields = [
            'uuid',
            'usuario',
            'ticket',
            'mensagem',
            'mensagem_relacionada',
            'solucao',
            'data_cadastro',
            'hora_cadastro',
        ]


class MensagemTicketSerializerCreate(MensagemTicketSerializer):
    usuario = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid')
    ticket = serializers.SlugRelatedField(queryset=Ticket.objects.all(), slug_field='uuid')
    mensagem_relacionada = serializers.PrimaryKeyRelatedField(queryset=MensagemTicket.objects.all(), allow_null=True)


class MensagemTicketSerializerRetrieve(MensagemTicketSerializer):
    usuario = UsuarioSerializerSimples(read_only=True)
    ticket = TicketSerializer(read_only=True)
    mensagem_relacionada = MensagemTicketSerializer(read_only=True)


class MensagemTicketSerializerRetrieveTicket(MensagemTicketSerializer):
    usuario = UsuarioSerializerSimples(read_only=True)
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    mensagem_relacionada = MensagemTicketSerializer(read_only=True)


class TicketSerializerRetrieve(TicketSerializer):
    solicitante = UsuarioSerializerSimples(read_only=True)
    atendente = UsuarioSerializerSimples(read_only=True)
    mensagens = MensagemTicketSerializerRetrieveTicket(many=True, source='ticket_ticket_mensagem_ticket', read_only=True)
    grupo = GrupoSerializer(read_only=True)
    subgrupo = SubgrupoSerializer(read_only=True)

    class Meta(TicketSerializer.Meta):
        fields = [
            'uuid',
            'status',
            'solicitante',
            'atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'avaliacao_atendente',
            'observacao_avaliacao_atendente',
            'data_cadastro',
            'hora_cadastro',
            'mensagens',
        ]
