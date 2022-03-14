from rest_framework import viewsets
from .models import Empresa
from .serializer import EmpresaSerializer
from .filters import EmpresaFilter
from .permissions import EmrpesaPemission


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    lookup_field = 'uuid'
    serializer_class = EmpresaSerializer
    filterset_class = EmpresaFilter
    permission_classes = (EmrpesaPemission, )
