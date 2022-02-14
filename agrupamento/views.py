from rest_framework import viewsets
from .models import Grupo, Subgrupo
from .serializer import GrupoSerializer, SubgrupoSerializer
from .filters import GrupoFilter, SubgrupoFilter


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    lookup_field = 'uuid'
    filterset_class = GrupoFilter
    serializer_class = GrupoSerializer


class SubgrupoViewSet(viewsets.ModelViewSet):
    queryset = Subgrupo.objects.all()
    lookup_field = 'uuid'
    filterset_class = SubgrupoFilter
    serializer_class = SubgrupoSerializer
