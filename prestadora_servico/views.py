from rest_framework import viewsets
from .models import PrestadoraServico
from .serializer import PrestadoraServicoSerializer


class PrestadoraServicoViewSet(viewsets.ModelViewSet):
    queryset = PrestadoraServico.objects.all()
    serializer_class = PrestadoraServicoSerializer
