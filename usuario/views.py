from rest_framework import viewsets, mixins
from .models import Usuario
from .filters import UsuarioFilter
from core.permissions import BasePemission
from django.contrib.auth.models import Group, Permission
from .serializer import UsuarioSerializer, UsuarioSerializerCreate, UsuarioSerializerRetrieve, \
                        UsuarioSerializerUpdatePartialUpdate, \
                        GrupoPermissoesUsuarioSerializer, \
                        PermissaoUsuarioSerializer, GrupoPermissoesUsuarioSerializerCreateUpdatePartialUpadate, \
                        GrupoPermissoesUsuarioSerializerRetrieve


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all() \
        .prefetch_related('classificacao') \
        .prefetch_related('empresa')
    filterset_class = UsuarioFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'create': UsuarioSerializerCreate,
        'retrieve': UsuarioSerializerRetrieve,
        'update': UsuarioSerializerUpdatePartialUpdate,
        'partial_update': UsuarioSerializerUpdatePartialUpdate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, UsuarioSerializer)


class GrupoPermissoesUsuarioViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GrupoPermissoesUsuarioSerializer
    permission_classes = (BasePemission, )

    serializer_classes = {
        'retrieve': GrupoPermissoesUsuarioSerializerRetrieve,
        'create': GrupoPermissoesUsuarioSerializerCreateUpdatePartialUpadate,
        'update': GrupoPermissoesUsuarioSerializerCreateUpdatePartialUpadate,
        'partial_update': GrupoPermissoesUsuarioSerializerCreateUpdatePartialUpadate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, GrupoPermissoesUsuarioSerializer)


class PermissaoUsuarioViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissaoUsuarioSerializer
    permission_classes = (BasePemission, )
