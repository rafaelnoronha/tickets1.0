from rest_framework import serializers
from .models import Usuario
from agrupamento.models import Classificacao
from agrupamento.serializer import ClassificacaoSerializer
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from empresa.models import Empresa
from empresa.serializer import EmpresaSerializer
import re


class UsuarioSerializer(serializers.ModelSerializer):
    sr_empresa = serializers.SlugRelatedField(read_only=True, slug_field='mp_nome_fantasia')
    groups = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
    sr_classificacao = serializers.SlugRelatedField(read_only=True, slug_field='cl_nome')

    def validate_is_staff(self, is_staff):
        empresa = Empresa.objects.get(id=self.initial_data['sr_empresa'])

        if is_staff:
            if not empresa.prestadora_servico:
                raise serializers.ValidationError("Não é possível salvar um usuário 'is_staff=true' se a empresa vinculada não estiver como 'prestadora_servico=false'")

        if not is_staff:
            if empresa.prestadora_servico:
                raise serializers.ValidationError("Não é possível salvar um usuário 'is_staff=false' se a empresa vinculada estiver como 'prestadora_servico=true'")

        return is_staff

    def validate_sr_empresa(self, sr_empresa):
        usuario = self.initial_data
        is_staff = usuario['is_staff'] if 'is_staff' in usuario else False

        if not sr_empresa.ativo:
            raise serializers.ValidationError("Não é possível salvar um usuário se a empresa vinculada está como 'ativo=false'")

        if sr_empresa.mp_prestadora_servico:
            if not is_staff:
                raise serializers.ValidationError("Não é possível salvar um usuário 'is_staff=false' se a empresa vinculada não estiver como 'prestadora_servico=true'")

        if not sr_empresa.mp_prestadora_servico:
            if is_staff:
                raise serializers.ValidationError("Não é possível salvar um usuário 'is_staff=true' se a empresa vinculada estiver como 'prestadora_servico=false'")

        return sr_empresa

    def validate_sr_classificacao(self, sr_classificacao):
        if not sr_classificacao.ativo:
            raise serializers.ValidationError("Não é possível salvar um usuário se a classificação vinculada está como 'ativo=false'")

        return sr_classificacao

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError("Sua senha deve ter no mínimo 6 caracteres")

        return make_password(password)

    class Meta:
        model = Usuario
        read_only_fields = [
            'id',
            'last_login',
            'sr_media_avaliacoes',
            'is_superuser',
            'is_staff',
            'sr_is_manager',
            'sr_empresa',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'sr_codigo_verificacao_segunda_etapa': {'write_only': True},
            'first_name': {'allow_null': False, 'allow_blank': False},
            'last_name': {'allow_null': False, 'allow_blank': False},
            'email': {'allow_null': False, 'allow_blank': False},
        }
        fields = [
            'id',
            'username',
            'password',
            'sr_codigo_verificacao_segunda_etapa',
            'first_name',
            'last_name',
            'email',
            'sr_telefone',
            'sr_celular',
            'sr_observacoes',
            'sr_media_avaliacoes',
            'sr_empresa',
            'last_login',
            'sr_classificacao',
            'is_staff',
            'sr_is_manager',
            'is_superuser',
            'is_active',
            'groups',
        ]


class UsuarioSerializerCreate(UsuarioSerializer):
    sr_empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True)
    sr_classificacao = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id', required=False)

    class Meta(UsuarioSerializer.Meta):
        read_only_fields = [
            'id',
            'last_login',
            'sr_media_avaliacoes',
        ]
        extra_kwargs = {
            'sr_codigo_verificacao_segunda_etapa': {'write_only': True},
            'is_staff': {'allow_null': False},
        }


class UsuarioSerializerUpdatePartialUpdate(UsuarioSerializer):
    sr_empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True)
    sr_classificacao = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id', required=False)

    class Meta(UsuarioSerializer.Meta):
        read_only_fields = [
            'id',
            'last_login',
            'sr_media_avaliacoes',
            'username',
            'is_staff',
            'is_superuser',
            'sr_empresa',
        ]


class UsuarioSerializerSimples(UsuarioSerializer):
    sr_empresa = serializers.SlugRelatedField(read_only=True, slug_field='id')
    groups = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
    sr_classificacao = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta(UsuarioSerializer.Meta):
        fields = [
            'id',
            'username',
            'email',
            'sr_empresa',
            'sr_classificacao',
            'is_staff',
            'sr_is_manager',
            'is_superuser',
            'groups',
        ]


class PermissaoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        read_only_fields = [
            'id',
            'name',
            'content_type',
            'codename',
        ]
        fields = [
            'id',
            'name',
            'content_type',
            'codename',
        ]


class GrupoPermissoesUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        read_only_fields = ['id',]
        fields = [
            'id',
            'name',
        ]


class GrupoPermissoesUsuarioSerializerCreateUpdatePartialUpadate(GrupoPermissoesUsuarioSerializer):
    permissions = serializers.SlugRelatedField(queryset=Permission.objects.all(), slug_field='id', many=True)

    class Meta(GrupoPermissoesUsuarioSerializer.Meta):
        fields = [
            'id',
            'name',
            'permissions',
        ]


class GrupoPermissoesUsuarioSerializerRetrieve(GrupoPermissoesUsuarioSerializer):
    permissions = PermissaoUsuarioSerializer(many=True)

    class Meta(GrupoPermissoesUsuarioSerializer.Meta):
        read_only_fields = ['id',]
        fields = [
            'id',
            'name',
            'permissions',
        ]


class UsuarioSerializerRetrieve(UsuarioSerializer):
    sr_empresa = EmpresaSerializer(read_only=True)
    groups = GrupoPermissoesUsuarioSerializer(read_only=True, many=True)
    sr_classificacao = ClassificacaoSerializer(read_only=True)
