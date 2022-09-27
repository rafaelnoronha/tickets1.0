from rest_framework import serializers
from .models import Ticket, MensagemTicket, MovimentoTicket
from usuario.serializer import UsuarioSerializerSimples, ClassificacaoSerializer
from usuario.models import Usuario, Classificacao
from agrupamento.models import Agrupamento
from agrupamento.serializer import AgrupamentoSerializer


class TicketSerializerAuditoria(serializers.ModelSerializer):
    solicitante = serializers.SlugRelatedField(read_only=True, slug_field='id')
    classificacao_atendente = serializers.SlugRelatedField(read_only=True, slug_field='id')
    atendente = serializers.SlugRelatedField(read_only=True, slug_field='id')
    grupo = serializers.SlugRelatedField(read_only=True, slug_field='id')
    subgrupo = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Ticket
        fields = '__all__'


class MensagemTicketSerializerAuditoria(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(read_only=True, slug_field='id')
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='id')
    mensagem_relacionada = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = MensagemTicket
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    solicitante = serializers.SlugRelatedField(read_only=True, slug_field='username')
    classificacao_atendente = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    atendente = serializers.SlugRelatedField(read_only=True, slug_field='username')
    grupo = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    subgrupo = serializers.SlugRelatedField(read_only=True, slug_field='nome')

    def valida_edicao_ticket(self):
        if self.instance and (self.instance.finalizado or self.instance.cancelado):
            raise serializers.ValidationError("Não é possível alterar um ticket finalizado ou cancelado")

    def validate(self, attrs):
        self.valida_edicao_ticket()

        return attrs

    def validate_solicitante(self, solicitante):
        if not solicitante.is_active:
            raise serializers.ValidationError("Solicitante inativo")

        if solicitante.is_staff:
            raise serializers.ValidationError("Solicitante cadastrado como atendente")

        return solicitante

    def validate_classificacao_atendente(self, classificacao_atendente):
        if classificacao_atendente and not classificacao_atendente.ativo:
            raise serializers.ValidationError("Classificacao inativa")

        return classificacao_atendente

    def validate_atendente(self, atendente):
        if atendente and not atendente.is_active:
            raise serializers.ValidationError("Atendente inativo")

        if atendente and not atendente.is_staff:
            raise serializers.ValidationError("Atendente cadastrado como solicitante")

        return atendente

    def validate_grupo(self, grupo):
        if grupo and not grupo.ativo:
            raise serializers.ValidationError("Grupo inativo")

        return grupo

    def validate_subgrupo(self, subgrupo):
        if subgrupo and not subgrupo.ativo:
            raise serializers.ValidationError("Subgrupo inativo")

        return subgrupo

    # def validate_solucionado(self, solucionado):
    #     if solucionado and not solucionado.solucao:
    #         raise serializers.ValidationError("A mensagem não é uma solução")

    #     return solucionado

    def validate_avaliacao_solicitante(self, avaliacao_solicitante):
        if self.instance.cancelado:
            raise serializers.ValidationError("Não é possível avaliar um ticket cancelado")

        if not self.instance.finalizado:
            raise serializers.ValidationError("Não é possível avaliar um ticket que não esteja finalizado")

        if not self.instance.atendente:
            raise serializers.ValidationError("Não é possível avaliar um ticket que não está atribuido a nenhum atendente")

        if self.instance.avaliacao_solicitante > 0:
            raise serializers.ValidationError("Não é possível avaliar um ticket que já está avaliado")

        return avaliacao_solicitante

    def validate_observacao_avaliacao_solicitante(self, observacao_avaliacao_solicitante):
        if self.instance.observacao_avaliacao_solicitante:
            raise serializers.ValidationError("Não é possível sobrescrever a observação de uma avaliação")

        return observacao_avaliacao_solicitante


    class Meta:
        model = Ticket
        read_only_fields = [
            'id',
            'status',
            'prioridade',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
        ]
        fields = [
            'id',
            'status',
            'prioridade',
            'solicitante',
            'classificacao_atendente',
            'atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerCreate(TicketSerializer):
    solicitante = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id')
    classificacao_atendente = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                            allow_null=True, required=False)
    atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', allow_null=True,
                                                required=False)
    grupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(tipo='G'), slug_field='id', allow_null=True,
                                            required=False)
    subgrupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(tipo='S'), slug_field='id', allow_null=True,
                                            required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'id',
            'status',
            'prioridade',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerUpdatePartialUpdate(TicketSerializer):
    classificacao_atendente = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                            allow_null=True, required=False)
    grupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(tipo='G'), slug_field='id', allow_null=True,
                                            required=False)
    subgrupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(tipo='S'), slug_field='id', allow_null=True,
                                            required=False)

    class Meta(TicketSerializer.Meta):
        _read_only_fields = TicketSerializer.Meta.fields.copy()
        _read_only_fields.remove('classificacao_atendente')
        _read_only_fields.remove('grupo')
        _read_only_fields.remove('subgrupo')

        read_only_fields = _read_only_fields


class TicketSerializerAtribuirAtendente(TicketSerializer):
    atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True,
                                                allow_null=False, allow_empty=False)

    class Meta(TicketSerializer.Meta):
        _read_only_fields = TicketSerializer.Meta.fields.copy()
        _read_only_fields.remove('atendente')

        read_only_fields = _read_only_fields


class TicketSerializerReclassificar(TicketSerializer):
    classificacao_atendente = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                            required=True, allow_null=True)

    class Meta(TicketSerializer.Meta):
        _read_only_fields = TicketSerializer.Meta.fields.copy()
        _read_only_fields.remove('classificacao_atendente')

        read_only_fields = _read_only_fields


class TicketSerializerAvaliar(TicketSerializer):
    class Meta(TicketSerializer.Meta):
        _read_only_fields = TicketSerializer.Meta.fields.copy()
        _read_only_fields.remove('avaliacao_solicitante')
        _read_only_fields.remove('observacao_avaliacao_solicitante')

        read_only_fields = _read_only_fields


# class TicketSerializerSolucionar(TicketSerializer):
#     solucionado = serializers.SlugRelatedField(queryset=MensagemTicket.objects.all(), slug_field='id',
#                                                 allow_null=True, allow_empty=False, required=False)

#     class Meta(TicketSerializer.Meta):
#         read_only_fields = [
#             'id',
#             'status',
#             'prioridade',
#             'solicitante',
#             'classificacao_atendente',
#             'atendente',
#             'titulo',
#             'descricao',
#             'grupo',
#             'subgrupo',
#             'finalizado',
#             'cancelado',
#             'motivo_cancelamento',
#             'avaliacao_solicitante',
#             'observacao_avaliacao_solicitante',
#             'data_cadastro',
#             'hora_cadastro',
#         ]


# class TicketSerializerFinalizar(TicketSerializer):
#     finalizado = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True,
#                                                 allow_null=False, allow_empty=False)

#     class Meta(TicketSerializer.Meta):
#         read_only_fields = [
#             'id',
#             'status',
#             'prioridade',
#             'solicitante',
#             'classificacao_atendente',
#             'atendente',
#             'titulo',
#             'descricao',
#             'grupo',
#             'subgrupo',
#             'solucionado',
#             'cancelado',
#             'motivo_cancelamento',
#             'avaliacao_solicitante',
#             'observacao_avaliacao_solicitante',
#             'data_cadastro',
#             'hora_cadastro',
#         ]


# class TicketSerializerCancelar(TicketSerializer):
#     cancelado = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', allow_null=False,
#                                                 allow_empty=False, required=True)
#     motivo_cancelamento = serializers.CharField(required=True, allow_null=False, allow_blank=True)

#     class Meta(TicketSerializer.Meta):
#         read_only_fields = [
#             'id',
#             'status',
#             'prioridade',
#             'solicitante',
#             'classificacao_atendente',
#             'atendente',
#             'titulo',
#             'descricao',
#             'grupo',
#             'subgrupo',
#             'solucionado',
#             'finalizado',
#             'avaliacao_solicitante',
#             'observacao_avaliacao_solicitante',
#             'data_cadastro',
#             'hora_cadastro',
#         ]


class MensagemTicketSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(read_only=True, slug_field='username')
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='id')
    mensagem_relacionada = serializers.SlugRelatedField(read_only=True, slug_field='id', allow_null=True,
                                                        required=False)

    def validate_usuario(self, usuario):
        mensagem = self.initial_data
        ticket = Ticket.objects.get(id=mensagem['ticket'])

        if usuario != ticket.solicitante and (ticket.atendente and usuario != ticket.atendente):
            raise serializers.ValidationError("Não é possível salvar uma mensagem com um usuário que não esteja "
                                              "vinculado ao ticket como solicitante ou atendente")

        if not usuario.is_active:
            raise serializers.ValidationError("Não é possível salvar uma mensagem com um usuário inativo")

    def validate_ticket(self, ticket):
        if ticket.finalizado or ticket.cancelado:
            raise serializers.ValidationError("Não é possível salvar uma mensagem para um ticket finalizado ou cancelado")

        return ticket

    def validate_solucao(self, solucao):
        mensagem = self.initial_data
        usuario = Usuario.objects.get(id=mensagem['usuario'])

        if solucao and not usuario.is_staff:
            raise serializers.ValidationError("Não é possível salvar uma mensagem como solução que tenha um usuário como solicitante")

        return solucao

    class Meta:
        model = MensagemTicket
        read_only_fields = [
            'id',
            'data_cadastro',
            'hora_cadastro',
        ]
        fields = [
            'id',
            'usuario',
            'ticket',
            'mensagem',
            'mensagem_relacionada',
            'solucao',
            'data_cadastro',
            'hora_cadastro',
        ]


class MensagemTicketSerializerCreate(MensagemTicketSerializer):
    usuario = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id')
    ticket = serializers.SlugRelatedField(queryset=Ticket.objects.all(), slug_field='id')
    mensagem_relacionada = serializers.SlugRelatedField(queryset=MensagemTicket.objects.all(), slug_field='id',
                                                        allow_null=True, required=False)


class MovimentoTicketSerializer(serializers.ModelSerializer):
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='id')
    classificacao_atendente = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    atendente = serializers.SlugRelatedField(read_only=True, slug_field='username')
    solucionado = serializers.SlugRelatedField(read_only=True, slug_field='id')
    finalizado = serializers.SlugRelatedField(read_only=True, slug_field='username')
    cancelado = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = MovimentoTicket
        fields = [
            'id',
            'ticket',
            'data_inicio',
            'hora_inicio',
            'data_fim',
            'hora_fim',
            'classificacao_atendente',
            'atendente',
            'solucionado',
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
            'data_cadastro',
            'hora_cadastro',
        ]
        read_only_fields = fields


class MensagemTicketSerializerRetrieveTicket(MensagemTicketSerializer):
    usuario = UsuarioSerializerSimples(read_only=True)
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='id')
    mensagem_relacionada = MensagemTicketSerializer(read_only=True)


class MensagemTicketSerializerRetrieve(MensagemTicketSerializer):
    usuario = UsuarioSerializerSimples(read_only=True)
    ticket = TicketSerializer(read_only=True)
    mensagem_relacionada = MensagemTicketSerializer(read_only=True)


class MovimentoTicketSerializerRetrieve(MovimentoTicketSerializer):
    ticket = TicketSerializer(read_only=True)
    classificacao_atendente = ClassificacaoSerializer(read_only=True)
    atendente = UsuarioSerializerSimples(read_only=True)
    solucionado = MensagemTicketSerializerRetrieveTicket(read_only=True)
    finalizado = UsuarioSerializerSimples(read_only=True)
    cancelado = UsuarioSerializerSimples(read_only=True)


class TicketSerializerRetrieve(TicketSerializer):
    solicitante = UsuarioSerializerSimples(read_only=True)
    classificacao_atendente = ClassificacaoSerializer(read_only=True)
    atendente = UsuarioSerializerSimples(read_only=True)
    mensagens = MensagemTicketSerializerRetrieveTicket(source='rl_ticket', many=True,
                                                        read_only=True)
    grupo = AgrupamentoSerializer(read_only=True)
    subgrupo = AgrupamentoSerializer(read_only=True)
    movimentos = MovimentoTicketSerializerRetrieve(source='rl_ticket', read_only=True, many=True)
