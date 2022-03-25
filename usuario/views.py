from rest_framework import viewsets, mixins
from .models import Usuario, LogAutenticacao
from .filters import UsuarioFilter, LogAutenticacaoFilter
from core.permissions import BasePemission
from django.contrib.auth.models import Group, Permission
from .serializer import UsuarioSerializer, UsuarioSerializerCreate, UsuarioSerializerRetrieve, \
                        UsuarioSerializerUpdatePartialUpdate, LogAutenticacaoSerializer, \
                        LogAutenticacaoSerializerRetrieve, GrupoPermissoesUsuarioSerializer, \
                        PermissaoUsuarioSerializer, GrupoPermissoesUsuarioSerializerCreateUpdatePartialUpadate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    lookup_field = 'uuid'
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


class LogAutenticacaoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = LogAutenticacao.objects.all()
    lookup_field = 'uuid'
    filterset_class = LogAutenticacaoFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'retrieve': LogAutenticacaoSerializerRetrieve
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LogAutenticacaoSerializer)


class GrupoPermissoesUsuarioViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GrupoPermissoesUsuarioSerializer
    permission_classes = (BasePemission, )

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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        #token['name'] = user.name
        # ...

        return token

    def validate(self, attrs):
        print(attrs)
        print(type(attrs))
        usuario_login = Usuario.objects.get(username='root')

        try:
            super().validate(attrs)
            usuario_login.numero_tentativas_login = 0
        except:
            usuario_login.numero_tentativas_login += 1

        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
