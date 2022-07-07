from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from core.views import ModelViewSetComAuditoria, CreateModelMixinAuditoria
from .models import Ticket, MensagemTicket, MovimentoTicket
from .filters import TicketFilter, MensagemTicketFilter, MovimentoTicketFilter
from core.permissions import BasePemission
from .serializer import TicketSerializer, TicketSerializerRetrieve, TicketSerializerCreate, \
                        TicketSerializerUpdatePartialUpdate, MensagemTicketSerializer, MensagemTicketSerializerCreate, \
                        MensagemTicketSerializerRetrieve, TicketSerializerAuditoria, MensagemTicketSerializerAuditoria, \
                        TicketSerializerFinalizar, TicketSerializerCancelar, TicketSerializerAvaliar, \
                        TicketSerializerSolucionar, TicketSerializerAtribuirAtendente, TicketSerializerReclassificar, \
                        MovimentoTicketSerializer, MovimentoTicketSerializerRetrieve


class TicketViewSet(ModelViewSetComAuditoria):
    queryset = Ticket.objects.all()
    lookup_field = 'uuid'
    filterset_class = TicketFilter
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Ticket,
        'nome_tabela': 'ticket',
        'serializer': TicketSerializerAuditoria,
    }

    serializer_classes = {
        'retrieve': TicketSerializerRetrieve,
        'create': TicketSerializerCreate,
        'update': TicketSerializerUpdatePartialUpdate,
        'partial_update': TicketSerializerUpdatePartialUpdate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, TicketSerializer)

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_superuser:
            return self.queryset

        if usuario.is_staff:
            if not usuario.is_manager:
                return Ticket.objects.filter(Q(atendente=usuario) | Q(atendente__isnull=True))

            return Ticket.objects.filter(Q(atendente__empresa=usuario.empresa) | Q(atendente__isnull=True))
        else:
            if usuario.is_manager:
                return Ticket.objects.filter(solicitante__empresa=usuario.empresa)
            else:
                return Ticket.objects.filter(solicitante=usuario)

    @action(detail=True, methods=['get'])
    def movimento(self, request, uuid):
        instance = self.get_object()
        movimentos = MovimentoTicket.objects.filter(ticket=instance)
        serializer = MovimentoTicketSerializer(movimentos, many=True)
        headers = self.get_success_headers(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def atribuir(self, request, uuid):
        instance = self.get_object()
        serializer = TicketSerializerAtribuirAtendente(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def reclassificar(self, request, uuid):
        instance = self.get_object()
        instance.atendente = None
        serializer = TicketSerializerReclassificar(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def solucionar(self, request, uuid):
        instance = self.get_object()
        serializer = TicketSerializerSolucionar(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def finalizar(self, request, uuid):
        instance = self.get_object()
        serializer = TicketSerializerFinalizar(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def avaliar(self, request, uuid):
        instance = self.get_object()
        serializer = TicketSerializerAvaliar(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def cancelar(self, request, uuid):
        instance = self.get_object()
        serializer = TicketSerializerCancelar(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class MensagemTicketViewSet(CreateModelMixinAuditoria, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = MensagemTicket.objects.all()
    lookup_field = 'uuid'
    filterset_class = MensagemTicketFilter
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': MensagemTicket,
        'nome_tabela': 'mensagem_ticket_serializer',
        'serializer': MensagemTicketSerializerAuditoria,
    }

    serializer_classes = {
        'create': MensagemTicketSerializerCreate,
        'retrieve': MensagemTicketSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, MensagemTicketSerializer)

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_superuser:
            return self.queryset

        if usuario.is_staff:
            if not usuario.is_manager:
                return MensagemTicket.objects.filter(ticket__atendente=usuario)

            return MensagemTicket.objects.filter(ticket__atendente__empresa=usuario.empresa)
        else:
            if usuario.is_manager:
                return MensagemTicket.objects.filter(ticket__solicitante__empresa=usuario.empresa)
            else:
                return MensagemTicket.objects.filter(ticket__solicitante=usuario)


class MovimentoTicketViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MovimentoTicket.objects.all()
    lookup_field = 'uuid'
    filterset_class = MovimentoTicketFilter
    permission_classes = (BasePemission,)

    serializer_classes = {
        'retrieve': MovimentoTicketSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, MovimentoTicketSerializer)
