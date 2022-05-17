from core.views import ModelViewSetComAuditoria
from .models import Grupo, Subgrupo
from .serializer import GrupoSerializer, SubgrupoSerializer, GrupoSerializerAuditoria, SubgrupoSerializerAuditoria
from .filters import GrupoFilter, SubgrupoFilter
from core.permissions import BasePemission


class GrupoViewSet(ModelViewSetComAuditoria):
    queryset = Grupo.objects.all()
    lookup_field = 'uuid'
    filterset_class = GrupoFilter
    serializer_class = GrupoSerializer
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Grupo,
        'nome_tabela': 'grupo',
        'serializer': GrupoSerializerAuditoria,
    }


class SubgrupoViewSet(ModelViewSetComAuditoria):
    queryset = Subgrupo.objects.all()
    lookup_field = 'uuid'
    filterset_class = SubgrupoFilter
    serializer_class = SubgrupoSerializer
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Subgrupo,
        'nome_tabela': 'subgrupo',
        'serializer': SubgrupoSerializerAuditoria,
    }
