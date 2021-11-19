from rest_framework import serializers
from .models import Ticket, MensagemTicket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class MensagemTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensagemTicket
        fields = '__all__'
