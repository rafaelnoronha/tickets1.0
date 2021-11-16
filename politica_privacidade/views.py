from rest_framework import viewsets
from .models import PoliticaPrivacidade
from .serializer import PoliticaPrivacidadeSerializer


class PoliticaPrivacidadeViewSet(viewsets.ModelViewSet):
    queryset = PoliticaPrivacidade.objects.all()
    serializer_class = PoliticaPrivacidadeSerializer
