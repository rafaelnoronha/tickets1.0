from rest_framework import viewsets, mixins
from .models import Usuario, LogAutenticacao
from core.views import ModelViewSetComAuditoria
from .filters import UsuarioFilter, LogAutenticacaoFilter
from core.permissions import BasePemission
from django.contrib.auth.models import Group, Permission
from .serializer import UsuarioSerializer, UsuarioSerializerCreate, UsuarioSerializerRetrieve, \
                        UsuarioSerializerUpdatePartialUpdate, LogAutenticacaoSerializer, \
                        LogAutenticacaoSerializerRetrieve, GrupoPermissoesUsuarioSerializer, \
                        PermissaoUsuarioSerializer, GrupoPermissoesUsuarioSerializerCreateUpdatePartialUpadate, \
                        UsuarioSerializerAuditoria, GrupoPermissoesUsuarioSerializerAuditoria, \
                        PermissaoUsuarioSerializerAuditoria


class UsuarioViewSet(ModelViewSetComAuditoria):
    queryset = Usuario.objects.all()
    lookup_field = 'uuid'
    filterset_class = UsuarioFilter
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Usuario,
        'nome_tabela': 'usuario',
        'serializer': UsuarioSerializerAuditoria,
    }

    serializer_classes = {
        'create': UsuarioSerializerCreate,
        'retrieve': UsuarioSerializerRetrieve,
        'update': UsuarioSerializerUpdatePartialUpdate,
        'partial_update': UsuarioSerializerUpdatePartialUpdate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, UsuarioSerializer)


class LogAutenticacaoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = LogAutenticacao.objects.all()
    lookup_field = 'uuid'
    filterset_class = LogAutenticacaoFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'retrieve': LogAutenticacaoSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LogAutenticacaoSerializer)


class GrupoPermissoesUsuarioViewSet(ModelViewSetComAuditoria):
    queryset = Group.objects.all()
    serializer_class = GrupoPermissoesUsuarioSerializer
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': Group,
        'nome_tabela': 'auth_group',
        'serializer': GrupoPermissoesUsuarioSerializerAuditoria,
    }

    serializer_classes = {
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
    auditoria = {
        'modelo': Permission,
        'nome_tabela': 'auth_permission',
        'serializer': PermissaoUsuarioSerializerAuditoria,
    }
