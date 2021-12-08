from rest_framework import serializers
from .models import Ticket, MensagemTicket
from usuario.serializer import UsuarioSerializer
from usuario.models import Usuario


class TicketSerializer(serializers.ModelSerializer):
    solicitante = serializers.SlugRelatedField(read_only=True, slug_field='username')
    atendente = serializers.SlugRelatedField(read_only=True, slug_field='username')

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
            'avaliacao_solicitante',
            'avaliacao_atendente',
            'data_cadastro'
        ]


class TicketSerializerRetrieve(TicketSerializer):
    solicitante = UsuarioSerializer(read_only=True)
    atendente = UsuarioSerializer(read_only=True)


class TicketSerializerCreate(TicketSerializer):
    solicitante = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    atendente = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta:
        model = Ticket
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'solicitante',
            'atendente',
            'titulo',
            'descricao',
        ]


class TicketSerializerPutPatch(TicketSerializer):
    class Meta:
        model = Ticket
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'avaliacao_solicitante',
            'avaliacao_atendente',
        ]


class MensagemTicketSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(read_only=True, slug_field='username')
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    mensagem_relacionada = serializers.SlugRelatedField(read_only=True, slug_field='uuid')

    class Meta:
        model = MensagemTicket
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'uuid',
            'usuario',
            'ticket',
            'mensagem',
            'mensagem_relacionada',
            'solucao',
        ]


class MensagemTicketSerializerCreate(MensagemTicketSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())
    mensagem_relacionada = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), allow_null=True)


class MensagemTicketSerializerRetrieve(MensagemTicketSerializer):
    usuario = UsuarioSerializer(read_only=True)
    ticket = TicketSerializer(read_only=True)
    mensagem_relacionada = MensagemTicketSerializer(read_only=True)
