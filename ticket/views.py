from rest_framework import viewsets
from .models import Ticket, MensagemTicket
from .serializer import TicketSerializer, TicketSerializerRetrieve, TicketSerializerCreate, TicketSerializerPutPatch, \
                        MensagemTicketSerializer, MensagemTicketSerializerCreate, MensagemTicketSerializerRetrieve


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    lookup_field = 'uuid'

    serializer_classes = {
        'retrieve': TicketSerializerRetrieve,
        'create': TicketSerializerCreate,
        'update': TicketSerializerPutPatch,
        'partial_update': TicketSerializerPutPatch,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, TicketSerializer)


class MensagemTicketViewSet(viewsets.ModelViewSet):
    queryset = MensagemTicket.objects.all()
    lookup_field = 'uuid'

    serializer_classes = {
        'create': MensagemTicketSerializerCreate,
        'retrieve': MensagemTicketSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, MensagemTicketSerializer)
