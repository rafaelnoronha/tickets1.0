from rest_framework import serializers
from django.core.exceptions import ValidationError
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
    solucionado = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    finalizado = serializers.SlugRelatedField(read_only=True, slug_field='uuid')

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
    solucionado = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    finalizado = serializers.SlugRelatedField(read_only=True, slug_field='username')

    def validate_solicitante(self, solicitante):
        if not solicitante.is_active:
            raise serializers.ValidationError("Não é possível salvar um ticket com um solicitante 'is_active=false'")

        if solicitante.is_staff:
            raise serializers.ValidationError("Não é possível salvar um ticket com um solicitante 'is_staff=true'")

        return solicitante

    def validate_atendente(self, atendente):
        if not atendente.is_active:
            raise serializers.ValidationError("Não é possível salvar um ticket com um atendente 'is_active=false'")

        if not atendente.is_staff:
            raise serializers.ValidationError("Não é possível salvar um ticket com um atendente 'is_staff=false'")

        return atendente

    def validate_grupo(self, grupo):
        if not grupo.ativo:
            raise serializers.ValidationError("Não é possível salvar um ticket com um grupo 'ativo=false'")

        return grupo

    def validate_subgrupo(self, subgrupo):
        if not subgrupo.ativo:
            raise serializers.ValidationError("Não é possível salvar um ticket com um subgrupo 'ativo=false'")

        return subgrupo

    def validate_solucionado(self, solucionado):
        if not solucionado.ativo:
            raise serializers.ValidationError("Não é possível salvar um ticket com o solucionado 'ativo=false'")

        return solucionado

    def validate_finalizado(self, finalizado):
        if not self.finalizado.ativo:
            raise serializers.ValidationError("Não é possível salvar um ticket com o finalizado 'ativo=false'")

        return finalizado

    class Meta:
        model = Ticket
        read_only_fields = [
            'uuid',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'data_solucao',
            'hora_solucao',
            'data_finalizacao',
            'hora_finalizacao',
        ]
        fields = [
            'uuid',
            'status',
            'solicitante',
            'atendente',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'solucionado',
            'data_solucao',
            'hora_solucao',
            'finalizado',
            'data_finalizacao',
            'hora_finalizacao',
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
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
        ]
        extra_kwargs = {
            'grupo': {'allow_null': True, 'allow_blank': True},
            'subgrupo': {'allow_null': True, 'allow_blank': True},
        }
        fields = [
            'uuid',
            'solicitante',
            'atendente',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
        ]


class TicketSerializerPutPatch(TicketSerializer):
    atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid')
    grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field='uuid', allow_null=True)
    subgrupo = serializers.SlugRelatedField(queryset=Subgrupo.objects.all(), slug_field='uuid', allow_null=True)
    solucionado = serializers.SlugRelatedField(queryset=MensagemTicket.objects.all(), slug_field='uuid', allow_null=True)

    class Meta:
        model = Ticket
        read_only_fields = [
            'uuid',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'solicitante',
            'titulo',
            'descricao',
            'data_solucao',
            'hora_solucao',
            'data_finalizacao',
            'hora_finalizacao',
            'data_cadastro',
            'hora_cadastro',

        ]
        fields = [
            'solicitante',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'atendente',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'solucao',
            'data_solucao',
            'hora_solucao',
            'finalizado',
            'data_finalizacao',
            'hora_finalizacao',
            'avaliacao_atendente',
            'observacao_avaliacao_atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'solucionado',
            'data_solucao',
            'hora_solucao',
            'finalizado',
            'data_finalizacao',
            'hora_finalizacao',
            'data_cadastro',
            'hora_cadastro',
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
    solucionado = MensagemTicketSerializerRetrieveTicket(source='solucionado_ticket_ticket', read_only=True)
    finalizado = UsuarioSerializerSimples(read_only=True)

    class Meta(TicketSerializer.Meta):
        fields = [
            'uuid',
            'status',
            'solicitante',
            'atendente',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'avaliacao_atendente',
            'observacao_avaliacao_atendente',
            'solucionado',
            'data_solucao',
            'hora_solucao',
            'finalizado',
            'data_finalizacao',
            'hora_finalizacao',
            'data_cadastro',
            'hora_cadastro',
            'mensagens',
        ]
