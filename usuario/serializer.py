from rest_framework import serializers
from .models import Usuario, LogAutenticacao
from django.contrib.auth.models import Group, Permission
from empresa.models import Empresa
from empresa.serializer import EmpresaSerializer


class UsuarioSerializerAuditoria(serializers.ModelSerializer):
    empresa = serializers.SlugRelatedField(read_only=True, slug_field='nome_fantasia')
    #groups = serializers.SlugRelatedField(read_only=True, slug_field='uuid', many=True)

    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    empresa = serializers.SlugRelatedField(read_only=True, slug_field='nome_fantasia')
    groups = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)

    class Meta:
        model = Usuario
        read_only_fields = [
            'uuid',
            'last_login',
            'media_avaliacoes',
            'is_superuser',
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
        ]


class UsuarioSerializerCreate(UsuarioSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='uuid')
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True)


class UsuarioSerializerUpdatePartialUpdate(UsuarioSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='uuid')
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True)

    class Meta(UsuarioSerializer.Meta):
        read_only_fields = [
            'uuid',
            'last_login',
            'media_avaliacoes',
            'username',
            'is_superuser',
        ]


class UsuarioSerializerSimples(UsuarioSerializer):
    empresa = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    groups = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)

    class Meta(UsuarioSerializer.Meta):
        fields = [
            'uuid',
            'username',
            'email',
            'empresa',
            'groups',
        ]


class LogAutenticacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(read_only=True, slug_field='username')

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


class LogAutenticacaoSerializerRetrieve(LogAutenticacaoSerializer):
    usuario = UsuarioSerializerSimples(read_only=True)


class PermissaoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            'id',
            'name',
            'content_type',
            'codename',
        ]


class GrupoPermissoesUsuarioSerializer(serializers.ModelSerializer):
    permissions = PermissaoUsuarioSerializer(many=True)

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'permissions',
        ]


class GrupoPermissoesUsuarioSerializerSimples(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
        ]


class GrupoPermissoesUsuarioSerializerCreateUpdatePartialUpadate(serializers.ModelSerializer):
    permissions = serializers.SlugRelatedField(queryset=Permission.objects.all(), slug_field='id', many=True)

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'permissions',
        ]


class UsuarioSerializerRetrieve(UsuarioSerializer):
    empresa = EmpresaSerializer(read_only=True)
    groups = GrupoPermissoesUsuarioSerializerSimples(read_only=True, many=True)