from rest_framework import viewsets, mixins
from .models import Usuario, LogAutenticacao
from .serializer import UsuarioSerializer, LogAutenticacaoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class LogAutenticacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = LogAutenticacao.objects.all()
    serializer_class = LogAutenticacaoSerializer
