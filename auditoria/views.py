from rest_framework import viewsets, mixins
from .models import Auditoria
from .serializer import AuditoriaSerializer, AuditoriaSerializerRetrieve
from .filters import AuditoriaFilter


class AuditoriaViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Auditoria.objects.all()
    lookup_field = 'uuid'
    filterset_class = AuditoriaFilter

    serializer_classes = {
        'retrieve': AuditoriaSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, AuditoriaSerializer)
