from rest_framework import viewsets
from .models import Usuario, LogAutenticacao
from .serializer import UsuarioSerializer, LogAutenticacaoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class LogAutenticacaoViewSet(viewsets.ModelViewSet):
    queryset = LogAutenticacao.objects.all()
    serializer_class = LogAutenticacaoSerializer
