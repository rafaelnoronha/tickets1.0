from rest_framework import viewsets
from core.views import ModelViewSetComAuditoria
from .models import Empresa
from .serializer import EmpresaSerializer, EmpresaSerializerAuditoria
from .filters import EmpresaFilter
from core.permissions import BasePemission


class EmpresaViewSet(ModelViewSetComAuditoria):
    queryset = Empresa.objects.all()
    lookup_field = 'uuid'
    serializer_class = EmpresaSerializer
    filterset_class = EmpresaFilter
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Empresa,
        'nome_tabela': 'empresa',
        'serializer': EmpresaSerializerAuditoria,
    }
