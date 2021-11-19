from rest_framework import viewsets
from .models import Auditoria
from .serializer import AuditoriaSerializer


class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer
