from rest_framework import viewsets
from .models import Empresa
from .serializer import EmpresaSerializer, EmpresaSerializerUpdatePartialUpdate
from .filters import EmpresaFilter
from core.permissions import BasePemission


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    filterset_class = EmpresaFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'update': EmpresaSerializerUpdatePartialUpdate,
        'partial_update': EmpresaSerializerUpdatePartialUpdate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, EmpresaSerializer)
