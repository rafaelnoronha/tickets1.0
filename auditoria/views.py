from rest_framework import viewsets, mixins
from .models import Auditoria
from .serializer import AuditoriaSerializer, AuditoriaSerializerRetrieve


class AuditoriaViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Auditoria.objects.all()
    lookup_field = 'uuid'

    serializer_classes = {
        'retrieve': AuditoriaSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, AuditoriaSerializer)
