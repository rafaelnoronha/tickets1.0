from rest_framework import serializers
from .models import Usuario, LogAutenticacao
from django.contrib.auth.models import Group, Permission
from empresa.models import Empresa
from empresa.serializer import EmpresaSerializer
from django.core.exceptions import ValidationError


class UsuarioSerializerAuditoria(serializers.ModelSerializer):
    empresa = serializers.SlugRelatedField(read_only=True, slug_field='uuid')

    class Meta:
        model = Usuario
        fields = '__all__'


class PermissaoUsuarioSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GrupoPermissoesUsuarioSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = Group
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
            'is_staff',
            'empresa',
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

    def validate(self, attrs):
        empresa = attrs['empresa']

        if attrs.__contains__('is_staff') and attrs['is_staff']:
            if not empresa.prestadora_servico:
                raise ValidationError("Não é possível salvar um usuário 'is_staff=true' se a empresa "
                                      "vinculada não estiver como 'prestadora_servico=false'")

        if attrs.__contains__('is_staff') and not attrs['is_staff']:
            if empresa.prestadora_servico:
                raise ValidationError("Não é possível salvar um usuário 'is_staff=false' se a empresa "
                                      "vinculada estiver como 'prestadora_servico=true'")

        if empresa.prestadora_servico:
            raise ValidationError("Não é possível salvar um usuário 'is_staff=false' se a empresa "
                                  "vinculada estiver como 'prestadora_servico=true'")

        return attrs


class UsuarioSerializerCreate(UsuarioSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='uuid')
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True)

    class Meta(UsuarioSerializer.Meta):
        read_only_fields = [
            'uuid',
            'last_login',
            'media_avaliacoes',
        ]
        extra_kwargs = {
            'codigo_verificacao_segunda_etapa': {'write_only': True},
            'is_staff': {'allow_null': False},
        }


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
            'is_staff',
            'empresa',
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
