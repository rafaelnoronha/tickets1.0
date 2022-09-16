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
    solucionado = serializers.SlugRelatedField(read_only=True, slug_field='id')
    finalizado = serializers.SlugRelatedField(read_only=True, slug_field='id')
    cancelado = serializers.SlugRelatedField(read_only=True, slug_field='id')

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
    solucionado = serializers.SlugRelatedField(read_only=True, slug_field='id')
    finalizado = serializers.SlugRelatedField(read_only=True, slug_field='username')
    cancelado = serializers.SlugRelatedField(read_only=True, slug_field='username')

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

    def validate_solucionado(self, solucionado):
        if solucionado and not solucionado.solucao:
            raise serializers.ValidationError("A mensagem não é uma solução")

        return solucionado

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

    def validate_finalizado(self, finalizado):
        ticket = self.instance

        if ticket.finalizado:
            raise serializers.ValidationError("Não é possível finalizar um ticket que já está finalizado")

        if finalizado != ticket.solicitante and (not ticket.atendente or ticket.atendente and finalizado != ticket.atendente):
            raise serializers.ValidationError("Não é possível finalizar um ticket com um usuário que não esteja vinculado ao ticket")

        if finalizado and not finalizado.is_active:
            raise serializers.ValidationError("Não é possível finalizar um ticket com um usuário inativo")

        if not ticket.solucionado:
            raise serializers.ValidationError("Não é possível finalizar um ticket que não esteja solucionado")

        return finalizado

    def validate_cancelado(self, cancelado):
        ticket = self.instance

        if ticket.cancelado:
            raise serializers.ValidationError("Não é possível cancelar um ticket já que já está cancelado")

        if 'motivo_cancelamento' not in self.get_initial():
            raise serializers.ValidationError("Não é possível cancelar um ticket sem informar o motivo do cancelamento")

        if cancelado != ticket.solicitante and (not ticket.atendente or ticket.atendente and cancelado !=
                                                ticket.atendente):
            raise serializers.ValidationError("Não é possível cancelar um ticket com um usuário que não esteja vinculado ao ticket")

        if cancelado and not cancelado.is_active:
            raise serializers.ValidationError("Não é possível finalizar um ticket com um usuário inativo")

        return cancelado

    def validate_motivo_cancelamento(self, motivo_cancelamento):
        if self.instance.cancelado:
            raise serializers.ValidationError("Não é possivel informar o motivo do cancelamento de um ticket cancelado")

        if self.instance.motivo_cancelamento:
            raise serializers.ValidationError("Não é possivel alterar o motivo do cancelamento")

        return motivo_cancelamento

    class Meta:
        model = Ticket
        read_only_fields = [
            'id',
            'status',
            'prioridade',
            'solucionado',
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
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
            'solucionado',
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
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
    grupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(tipo='GRP'), slug_field='id', allow_null=True,
                                            required=False)
    subgrupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(tipo='SGR'), slug_field='id', allow_null=True,
                                            required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'id',
            'status',
            'prioridade',
            'solucionado',
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerUpdatePartialUpdate(TicketSerializer):
    classificacao_atendente = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                            allow_null=True, required=False)
    grupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(tipo='GRP'), slug_field='id', allow_null=True,
                                            required=False)
    subgrupo = serializers.SlugRelatedField(queryset=Agrupamento.objects.filter(tipo='SGR'), slug_field='id', allow_null=True,
                                            required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'id',
            'status',
            'prioridade',
            'solicitante',
            'atendente',
            'titulo',
            'descricao',
            'solucionado',
            'finalizado',
            'cancelado',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerAtribuirAtendente(TicketSerializer):
    atendente = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True,
                                                allow_null=False, allow_empty=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'id',
            'status',
            'prioridade',
            'solicitante',
            'classificacao_atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerReclassificar(TicketSerializer):
    classificacao_atendente = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                            required=True, allow_null=True)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
            'id',
            'status',
            'prioridade',
            'solicitante',
            'atendente',
            'titulo',
            'descricao',
            'grupo',
            'subgrupo',
            'solucionado',
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerSolucionar(TicketSerializer):
    solucionado = serializers.SlugRelatedField(queryset=MensagemTicket.objects.all(), slug_field='id',
                                                allow_null=True, allow_empty=False, required=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
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
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerFinalizar(TicketSerializer):
    finalizado = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', required=True,
                                                allow_null=False, allow_empty=False)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
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
            'solucionado',
            'cancelado',
            'motivo_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerAvaliar(TicketSerializer):
    class Meta(TicketSerializer.Meta):
        read_only_fields = [
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
            'solucionado',
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
            'data_cadastro',
            'hora_cadastro',
        ]


class TicketSerializerCancelar(TicketSerializer):
    cancelado = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id', allow_null=False,
                                                allow_empty=False, required=True)
    motivo_cancelamento = serializers.CharField(required=True, allow_null=False, allow_blank=True)

    class Meta(TicketSerializer.Meta):
        read_only_fields = [
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
            'solucionado',
            'finalizado',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'data_cadastro',
            'hora_cadastro',
        ]


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


class MensagemTicketSerializerRetrieve(MensagemTicketSerializer):
    usuario = UsuarioSerializerSimples(read_only=True)
    ticket = TicketSerializer(read_only=True)
    mensagem_relacionada = MensagemTicketSerializer(read_only=True)


class MensagemTicketSerializerRetrieveTicket(MensagemTicketSerializer):
    usuario = UsuarioSerializerSimples(read_only=True)
    ticket = serializers.SlugRelatedField(read_only=True, slug_field='id')
    mensagem_relacionada = MensagemTicketSerializer(read_only=True)


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
            'data_cadastro',
            'hora_cadastro',
        ]
        read_only_fields = fields


class MovimentoTicketSerializerRetrieve(MovimentoTicketSerializer):
    ticket = TicketSerializer(read_only=True)
    classificacao_atendente = ClassificacaoSerializer(read_only=True)
    atendente = UsuarioSerializerSimples(read_only=True)
    solucionado = MensagemTicketSerializerRetrieveTicket(read_only=True)
    finalizado = UsuarioSerializerSimples(read_only=True)
    cancelado = UsuarioSerializerSimples(read_only=True)

    class Meta(MovimentoTicketSerializer.Meta):
        pass


class TicketSerializerRetrieve(TicketSerializer):
    solicitante = UsuarioSerializerSimples(read_only=True)
    classificacao_atendente = ClassificacaoSerializer(read_only=True)
    atendente = UsuarioSerializerSimples(read_only=True)
    mensagens = MensagemTicketSerializerRetrieveTicket(source='ticket_ticket_mensagem_ticket', many=True,
                                                        read_only=True)
    grupo = AgrupamentoSerializer(read_only=True)
    subgrupo = AgrupamentoSerializer(read_only=True)
    solucionado = MensagemTicketSerializerRetrieveTicket(read_only=True)
    finalizado = UsuarioSerializerSimples(read_only=True)
    cancelado = UsuarioSerializerSimples(read_only=True)
    movimentos = MovimentoTicketSerializerRetrieve(source='ticket_ticket_movimento_ticket', read_only=True, many=True)

    class Meta(TicketSerializer.Meta):
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
            'solucionado',
            'finalizado',
            'cancelado',
            'motivo_cancelamento',
            'avaliacao_solicitante',
            'observacao_avaliacao_solicitante',
            'mensagens',
            'movimentos',
            'data_cadastro',
            'hora_cadastro',
        ]
