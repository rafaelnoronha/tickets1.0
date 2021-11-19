from rest_framework import viewsets
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from .serializer import PoliticaPrivacidadeSerializer, ConsentimentoPoliticaPrivacidadeSerializer


class PoliticaPrivacidadeViewSet(viewsets.ModelViewSet):
    queryset = PoliticaPrivacidade.objects.all()
    serializer_class = PoliticaPrivacidadeSerializer


class ConsentimentoPoliticaPrivacidadeViewSet(viewsets.ModelViewSet):
    queryset = ConsentimentoPoliticaPrivacidade.objects.all()
    serializer_class = ConsentimentoPoliticaPrivacidadeSerializer
