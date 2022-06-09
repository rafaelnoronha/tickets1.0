from rest_framework import viewsets, mixins
from django.db.models import Q
from core.views import ModelViewSetComAuditoria, CreateModelMixinAuditoria
from .models import Ticket, MensagemTicket
from .filters import TicketFilter, MensagemTicketFilter
from core.permissions import BasePemission
from .serializer import TicketSerializer, TicketSerializerRetrieve, TicketSerializerCreate, TicketSerializerUpdatePartialUpdate, \
                        MensagemTicketSerializer, MensagemTicketSerializerCreate, MensagemTicketSerializerRetrieve, \
                        TicketSerializerAuditoria, MensagemTicketSerializerAuditoria


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
