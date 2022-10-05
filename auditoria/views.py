from rest_framework import viewsets, mixins
from .models import Auditoria, LogAutenticacao
from .serializer import AuditoriaSerializer, AuditoriaSerializerRetrieve, LogAutenticacaoSerializer, LogAutenticacaoSerializerRetrieve
from .filters import AuditoriaFilter, LogAutenticacaoFilter
from core.permissions import BasePemission


class AuditoriaViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Auditoria.objects.all() \
        .prefetch_related('dt_usuario_operacao')
    filterset_class = AuditoriaFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'retrieve': AuditoriaSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, AuditoriaSerializer)


class LogAutenticacaoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = LogAutenticacao.objects.all() \
        .prefetch_related('lg_usuario')
    filterset_class = LogAutenticacaoFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'retrieve': LogAutenticacaoSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LogAutenticacaoSerializer)

