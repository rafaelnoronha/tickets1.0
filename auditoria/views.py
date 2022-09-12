from rest_framework import viewsets, mixins
from .models import Auditoria
from .serializer import AuditoriaSerializer, AuditoriaSerializerRetrieve
from .filters import AuditoriaFilter
from core.permissions import BasePemission


class AuditoriaViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Auditoria.objects \
        .prefetch_related('usuario_operacao') \
        .all()
    filterset_class = AuditoriaFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'retrieve': AuditoriaSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, AuditoriaSerializer)
