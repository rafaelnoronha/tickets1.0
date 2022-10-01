from rest_framework import viewsets
from .models import Agrupamento, Classificacao
from .serializer import AgrupamentoSerializer, ClassificacaoSerializer
from .filters import AgrupamentoFilter, ClassificacaoFilter
from core.permissions import BasePemission


class AgrupamentoViewSet(viewsets.ModelViewSet):
    queryset = Agrupamento.objects.all()
    filterset_class = AgrupamentoFilter
    serializer_class = AgrupamentoSerializer
    permission_classes = (BasePemission, )


class ClassificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer
    filterset_class = ClassificacaoFilter
    permission_classes = (BasePemission, )
