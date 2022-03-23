from rest_framework import viewsets
from .models import Grupo, Subgrupo
from .serializer import GrupoSerializer, SubgrupoSerializer
from .filters import GrupoFilter, SubgrupoFilter
from core.permissions import BasePemission


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    lookup_field = 'uuid'
    filterset_class = GrupoFilter
    serializer_class = GrupoSerializer
    permission_classes = (BasePemission, )


class SubgrupoViewSet(viewsets.ModelViewSet):
    queryset = Subgrupo.objects.all()
    lookup_field = 'uuid'
    filterset_class = SubgrupoFilter
    serializer_class = SubgrupoSerializer
    permission_classes = (BasePemission, )
