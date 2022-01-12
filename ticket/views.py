from rest_framework import viewsets, mixins
from .models import Ticket, MensagemTicket
from .filters import TicketFilter, MensagemTicketFilter
from .serializer import TicketSerializer, TicketSerializerRetrieve, TicketSerializerCreate, TicketSerializerPutPatch, \
                        MensagemTicketSerializer, MensagemTicketSerializerCreate, MensagemTicketSerializerRetrieve


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    lookup_field = 'uuid'
    filterset_class = TicketFilter

    serializer_classes = {
        'retrieve': TicketSerializerRetrieve,
        'create': TicketSerializerCreate,
        'update': TicketSerializerPutPatch,
        'partial_update': TicketSerializerPutPatch,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, TicketSerializer)


class MensagemTicketViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    queryset = MensagemTicket.objects.all()
    lookup_field = 'uuid'

    serializer_classes = {
        'create': MensagemTicketSerializerCreate,
        'retrieve': MensagemTicketSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, MensagemTicketSerializer)
