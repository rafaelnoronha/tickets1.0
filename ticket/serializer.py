from rest_framework import serializers
from .models import Ticket, MensagemTicket, MovimentoTicket
from usuario.serializer import UsuarioSerializerSimples
from usuario.models import Usuario
from agrupamento.models import Agrupamento, Classificacao
from agrupamento.serializer import AgrupamentoSerializer, ClassificacaoSerializer


class TicketSerializer(serializers.ModelSerializer):
    tc_solicitante = serializers.SlugRelatedField(read_only=True, slug_field='username')
    tc_classificacao_atendente = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    tc_atendente = serializers.SlugRelatedField(read_only=True, slug_field='username')
    tc_grupo = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    tc_subgrupo = serializers.SlugRelatedField(read_only=True, slug_field='nome')

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
        fields = [
            'id',
            'tc_status',
            'tc_prioridade',
            'tc_solicitante',
            'tc_classificacao_atendente',
            'tc_atendente',
            'tc_titulo',
            'tc_descricao',
            'tc_grupo',
            'tc_subgrupo',
            'tc_avaliacao_solicitante',
            'tc_observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]
        read_only_fields = [
            'id',
            'tc_status',
            'tc_prioridade',
            'tc_avaliacao_solicitante',
            'tc_observacao_avaliacao_solicitante',
        ]


class TicketSerializerCreate(TicketSerializer):
    tc_solicitante = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id')
    tc_classificacao_atendente = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                            allow_null=True, required=False)
    tc_atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', allow_null=True,
                                                required=False)
    tc_grupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(gr_tipo='G'), slug_field='id', allow_null=True,
                                            required=False)
    tc_subgrupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(gr_tipo='S'), slug_field='id', allow_null=True,
                                            required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'id',
            'tc_status',
            'tc_prioridade',
            'tc_avaliacao_solicitante',
            'tc_observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerUpdatePartialUpdate(TicketSerializer):
    tc_classificacao_atendente = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                            allow_null=True, required=False)
    tc_grupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(gr_tipo='G'), slug_field='id', allow_null=True,
                                            required=False)
    tc_subgrupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(gr_tipo='S'), slug_field='id', allow_null=True,
                                            required=False)

    class Meta(TicketSerializer.Meta):
        _read_only_fields = TicketSerializer.Meta.fields.copy()
        _read_only_fields.remove('tc_classificacao_atendente')
        _read_only_fields.remove('tc_grupo')
        _read_only_fields.remove('tc_subgrupo')

        read_only_fields = _read_only_fields


class TicketSerializerAtribuirAtendente(TicketSerializer):
    tc_atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True,
                                                allow_null=False, allow_empty=False)

    class Meta(TicketSerializer.Meta):
        _read_only_fields = TicketSerializer.Meta.fields.copy()
        _read_only_fields.remove('tc_atendente')

        read_only_fields = _read_only_fields


class TicketSerializerReclassificar(TicketSerializer):
    tc_classificacao_atendente = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                            required=True, allow_null=True)

    class Meta(TicketSerializer.Meta):
        _read_only_fields = TicketSerializer.Meta.fields.copy()
        _read_only_fields.remove('tc_classificacao_atendente')

        read_only_fields = _read_only_fields


class TicketSerializerAvaliar(TicketSerializer):
    class Meta(TicketSerializer.Meta):
        _read_only_fields = TicketSerializer.Meta.fields.copy()
        _read_only_fields.remove('tc_avaliacao_solicitante')
        _read_only_fields.remove('tc_observacao_avaliacao_solicitante')

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
    mn_usuario = serializers.SlugRelatedField(read_only=True, slug_field='username')
    mn_ticket = serializers.SlugRelatedField(read_only=True, slug_field='id')
    mn_mensagem_relacionada = serializers.SlugRelatedField(read_only=True, slug_field='id', allow_null=True,
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
        fields = [
            'id',
            'mn_usuario',
            'mn_ticket',
            'mn_mensagem',
            'mn_mensagem_relacionada',
            'mn_solucao',
            'data_cadastro',
            'hora_cadastro',
        ]
        read_only_fields = [
            'id',
            'data_cadastro',
            'hora_cadastro',
        ]


class MensagemTicketSerializerCreate(MensagemTicketSerializer):
    mn_usuario = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id')
    mn_ticket = serializers.SlugRelatedField(queryset=Ticket.objects.all(), slug_field='id')
    mn_mensagem_relacionada = serializers.SlugRelatedField(queryset=MensagemTicket.objects.all(), slug_field='id',
                                                        allow_null=True, required=False)


class MovimentoTicketSerializer(serializers.ModelSerializer):
    mv_ticket = serializers.SlugRelatedField(read_only=True, slug_field='id')
    mv_classificacao_atendente = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    mv_atendente = serializers.SlugRelatedField(read_only=True, slug_field='username')
    mv_solucionado = serializers.SlugRelatedField(read_only=True, slug_field='id')
    mv_finalizado = serializers.SlugRelatedField(read_only=True, slug_field='username')
    mv_cancelado = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = MovimentoTicket
        fields = [
            'id',
            'mv_ticket',
            'mv_data_inicio',
            'mv_hora_inicio',
            'mv_data_fim',
            'mv_hora_fim',
            'mv_classificacao_atendente',
            'mv_atendente',
            'mv_solucionado',
            'mv_finalizado',
            'mv_cancelado',
            'mv_motivo_cancelamento',
            'data_cadastro',
            'hora_cadastro',
        ]
        read_only_fields = fields


class MensagemTicketSerializerRetrieveTicket(MensagemTicketSerializer):
    mn_usuario = UsuarioSerializerSimples(read_only=True)
    mn_ticket = serializers.SlugRelatedField(read_only=True, slug_field='id')
    mn_mensagem_relacionada = MensagemTicketSerializer(read_only=True)


class MensagemTicketSerializerRetrieve(MensagemTicketSerializer):
    mn_usuario = UsuarioSerializerSimples(read_only=True)
    mn_ticket = TicketSerializer(read_only=True)
    mn_mensagem_relacionada = MensagemTicketSerializer(read_only=True)


class MovimentoTicketSerializerRetrieve(MovimentoTicketSerializer):
    mv_ticket = TicketSerializer(read_only=True)
    mv_classificacao_atendente = ClassificacaoSerializer(read_only=True)
    mv_atendente = UsuarioSerializerSimples(read_only=True)
    mv_solucionado = MensagemTicketSerializerRetrieveTicket(read_only=True)
    mv_finalizado = UsuarioSerializerSimples(read_only=True)
    mv_cancelado = UsuarioSerializerSimples(read_only=True)


class TicketSerializerRetrieve(TicketSerializer):
    tc_solicitante = UsuarioSerializerSimples(read_only=True)
    tc_classificacao_atendente = ClassificacaoSerializer(read_only=True)
    tc_atendente = UsuarioSerializerSimples(read_only=True)
    tc_mensagens = MensagemTicketSerializerRetrieveTicket(source='rl_ticket', many=True,
                                                        read_only=True)
    tc_grupo = AgrupamentoSerializer(read_only=True)
    tc_subgrupo = AgrupamentoSerializer(read_only=True)
    tc_movimentos = MovimentoTicketSerializerRetrieve(source='rl_ticket', read_only=True, many=True)
