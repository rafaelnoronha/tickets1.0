from rest_framework import viewsets
from .models import Ticket, MensagemTicket
from .serializer import TicketSerializer, MensagemTicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class MensagemTicketViewSet(viewsets.ModelViewSet):
    queryset = MensagemTicket.objects.all()
    serializer_class = MensagemTicketSerializer
