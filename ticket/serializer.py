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
    solucionado = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    finalizado = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    cancelado = serializers.SlugRelatedField(read_only=True, slug_field='uuid')

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
    cancelado = serializers.SlugRelatedField(read_only=True, slug_field='username')

    def valida_edicao_ticket(self):
        if self.instance and (self.instance.finalizado or self.instance.cancelado):
            raise serializers.ValidationError("Não é possível alterar um ticket finalizado ou cancelado")

    def validate_solicitante(self, solicitante):
        if not solicitante.is_active:
            raise serializers.ValidationError("Não é possível salvar um ticket com um solicitante inativo")

        if solicitante.is_staff:
            raise serializers.ValidationError("Não é possível salvar um ticket com um solicitante 'is_staff=true'")

        return solicitante

    def validate_atendente(self, atendente):
        if atendente and not atendente.is_active:
            raise serializers.ValidationError("Não é possível salvar um ticket com um atendente inativo")

        if atendente and not atendente.is_staff:
            raise serializers.ValidationError("Não é possível salvar um ticket com um atendente 'is_staff=false'")

        return atendente

    def validate_grupo(self, grupo):
        self.valida_edicao_ticket()

        if grupo and not grupo.ativo:
            raise serializers.ValidationError("Não é possível salvar um ticket com um grupo inativo")

        return grupo

    def validate_subgrupo(self, subgrupo):
        self.valida_edicao_ticket()

        if subgrupo and not subgrupo.ativo:
            raise serializers.ValidationError("Não é possível salvar um ticket com um subgrupo inativo")

        return subgrupo

    def validate_solucionado(self, solucionado):
        self.valida_edicao_ticket()

        if solucionado and not solucionado.solucao:
            raise serializers.ValidationError("Não é possível salvar um ticket com uma solução setada como "
                                              "'solucao=false'")

        if solucionado and not solucionado.usuario.is_staff:
            raise serializers.ValidationError("Não é possível salvar um ticket com uma solução em que o usuario esteja "
                                              "como 'is_staff=false'")

        return solucionado

    def validate_avaliacao_solicitante(self, avaliacao_solicitante):
        if self.instance.cancelado:
            raise serializers.ValidationError("Não é possível avaliar um ticket cancelado")

        if not self.instance.atendente:
            raise serializers.ValidationError("Não é possível avaliar um ticket que não está atribuido a nenhum "
                                              "atendente")

        if self.instance.avaliacao_solicitante is not None:
            raise serializers.ValidationError("Não é possível avaliar um ticket que já está avaliado")

        return avaliacao_solicitante

    def validate_observacao_avaliacao_solicitante(self, observacao_avaliacao_solicitante):
        if self.instance.observacao_avaliacao_solicitante:
            raise serializers.ValidationError("Não é possível sobrescrever a observacao de uma avaliação")

        return observacao_avaliacao_solicitante

    def validate_finalizado(self, finalizado):
        self.valida_edicao_ticket()

        return finalizado

    def validate_cancelado(self, cancelado):
        self.valida_edicao_ticket()

        if self.instance.cancelado:
            raise serializers.ValidationError("Não é possível cancelar um ticket já está cancelado")

        return cancelado

    def validate_motivo_cancelamento(self, motivo_cancelamento):
        self.valida_edicao_ticket()

        if self.instance.cancelado:
            raise serializers.ValidationError("Não é possivel informar o motivo do cancelamento de um ticket cancelado")

        if self.instance.motivo_cancelamento:
            raise serializers.ValidationError("Não é possivel alterar o motivo do cancelamento")

        return motivo_cancelamento

    class Meta:
        model = Ticket
        read_only_fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'solucionado',
            'data_solucao',
            'hora_solucao',
            'finalizado',
            'data_finalizacao',
            'hora_finalizacao',
            'cancelado',
            'motivo_cancelamento',
            'data_cancelamento',
            'hora_cancelamento',
        ]
        fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
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
            'cancelado',
            'motivo_cancelamento',
            'data_cancelamento',
            'hora_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerCreate(TicketSerializer):
    solicitante = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid')
    atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid', allow_null=True,
                                             required=False)
    grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field='uuid', allow_null=True,
                                         required=False)
    subgrupo = serializers.SlugRelatedField(queryset=Subgrupo.objects.all(), slug_field='uuid', allow_null=True,
                                            required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'solucionado',
            'data_solucao',
            'hora_solucao',
            'finalizado',
            'data_finalizacao',
            'hora_finalizacao',
            'cancelado',
            'motivo_cancelamento',
            'data_cancelamento',
            'hora_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerUpdatePartialUpdate(TicketSerializer):
    atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid', required=False,
                                             allow_null=True)
    grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field='uuid', allow_null=True,
                                         required=False)
    subgrupo = serializers.SlugRelatedField(queryset=Subgrupo.objects.all(), slug_field='uuid', allow_null=True,
                                            required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
            'solicitante',
            'atendente',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'titulo',
            'descricao',
            'data_solucao',
            'hora_solucao',
            'finalizado',
            'data_finalizacao',
            'hora_finalizacao',
            'data_cancelamento',
            'hora_cancelamento',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerFinalizar(TicketSerializer):
    finalizado = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid', required=True,
                                              allow_null=False, allow_empty=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
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
            'data_finalizacao',
            'hora_finalizacao',
            'cancelado',
            'motivo_cancelamento',
            'data_cancelamento',
            'hora_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerCancelar(TicketSerializer):
    cancelado = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid', allow_null=False,
                                             allow_empty=False, required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
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
            'data_cancelamento',
            'hora_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerAvaliar(TicketSerializer):
    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
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
            'cancelado',
            'motivo_cancelamento',
            'data_cancelamento',
            'hora_cancelamento',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerSolucionar(TicketSerializer):
    solucionado = serializers.SlugRelatedField(queryset=MensagemTicket.objects.all(), slug_field='uuid',
                                               allow_null=True, allow_empty=False, required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
            'solicitante',
            'atendente',
            'data_atribuicao_atendente',
            'hora_atribuicao_atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'data_solucao',
            'hora_solucao',
            'finalizado',
            'data_finalizacao',
            'hora_finalizacao',
            'cancelado',
            'motivo_cancelamento',
            'data_cancelamento',
            'hora_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class MensagemTicketSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(read_only=True, slug_field='username')
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    mensagem_relacionada = serializers.SlugRelatedField(read_only=True, slug_field='uuid', allow_null=True,
                                                        required=False)

    def validate_usuario(self, usuario):
        mensagem = self.initial_data

        if 'solucao' in mensagem and mensagem['solucao'] and not usuario.is_staff:
            raise serializers.ValidationError("Não é possível salvar uma mensagem_ticket com um usuário "
                                              "'is_staff=false'")

        return usuario

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
    mensagem_relacionada = serializers.SlugRelatedField(queryset=MensagemTicket.objects.all(), slug_field='uuid',
                                                        allow_null=True, required=False)


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
    mensagens = MensagemTicketSerializerRetrieveTicket(source='ticket_ticket_mensagem_ticket', many=True,
                                                       read_only=True)
    grupo = GrupoSerializer(read_only=True)
    subgrupo = SubgrupoSerializer(read_only=True)
    solucionado = MensagemTicketSerializerRetrieveTicket(read_only=True)
    finalizado = UsuarioSerializerSimples(read_only=True)
    cancelado = UsuarioSerializerSimples(read_only=True)

    class Meta(TicketSerializer.Meta):
        fields = [
            'uuid',
            'codigo',
            'status',
            'prioridade',
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
            'cancelado',
            'motivo_cancelamento',
            'data_cancelamento',
            'hora_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'mensagens',
            'data_cadastro',
            'hora_cadastro',
        ]
