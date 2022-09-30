from rest_framework import viewsets
from .models import Empresa
from .serializer import EmpresaSerializer, EmpresaSerializerAuditoria, EmpresaSerializerUpdatePartialUpdate
from .filters import EmpresaFilter
from core.permissions import BasePemission


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    filterset_class = EmpresaFilter
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Empresa,
        'nome_tabela': 'empresa',
        'serializer': EmpresaSerializerAuditoria,
    }

    serializer_classes = {
        'update': EmpresaSerializerUpdatePartialUpdate,
        'partial_update': EmpresaSerializerUpdatePartialUpdate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, EmpresaSerializer)
