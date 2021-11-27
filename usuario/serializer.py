from rest_framework import serializers
from .models import Usuario, LogAutenticacao
from empresa.models import Empresa
from empresa.serializer import EmpresaSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    empresa = serializers.SlugRelatedField(read_only=True, slug_field='nome_fantasia')

    class Meta:
        model = Usuario
        read_only_fields = [
            'uuid',
            'last_login',
            'media_avaliacoes',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'codigo_verificacao_segunda_etapa': {'write_only': True},
            'first_name': {'allow_null': False, 'allow_blank': False},
            'last_name': {'allow_null': False, 'allow_blank': False},
            'email': {'allow_null': False, 'allow_blank': False},
        }
        fields = [
            'uuid',
            'username',
            'password',
            'codigo_verificacao_segunda_etapa',
            'first_name',
            'last_name',
            'email',
            'telefone',
            'celular',
            'observacoes',
            'media_avaliacoes',
            'empresa',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
        ]


class UsuarioSerializerCreate(UsuarioSerializer):
    empresa = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.all())


class UsuarioSerializerRetrieve(UsuarioSerializer):
    empresa = EmpresaSerializer(read_only=True)


class LogAutenticacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAutenticacao
        read_only_fields = ['uuid']
        fields = [
            'uuid',
            'ip',
            'autenticado',
            'data_autenticacao',
            'hora_autenticacao',
            'usuario',
        ]
