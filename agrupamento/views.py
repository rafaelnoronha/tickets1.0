from core.views import ModelViewSetComAuditoria
from .models import Agrupamento
from .serializer import AgrupamentoSerializer, AgrupamentoSerializerAuditoria
from .filters import AgrupamentoFilter
from core.permissions import BasePemission


class AgrupamentoViewSet(ModelViewSetComAuditoria):
    queryset = Agrupamento.objects.all()
    filterset_class = AgrupamentoFilter
    serializer_class = AgrupamentoSerializer
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Agrupamento,
        'nome_tabela': 'agrupamento',
        'serializer': AgrupamentoSerializerAuditoria,
    }
