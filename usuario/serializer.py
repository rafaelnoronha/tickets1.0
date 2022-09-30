from rest_framework import serializers
from .models import Usuario, Classificacao, LogAutenticacao
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.hashers import make_password
from empresa.models import Empresa
from empresa.serializer import EmpresaSerializer
import re


class UsuarioSerializerAuditoria(serializers.ModelSerializer):
    empresa = serializers.SlugRelatedField(read_only=True, slug_field='id')
    classificacao = serializers.SlugRelatedField(read_only=True, slug_field='id')

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
    classificacao = serializers.SlugRelatedField(read_only=True, slug_field='nome')

    def validate_is_staff(self, is_staff):
        empresa = Empresa.objects.get(id=self.initial_data['empresa'])

        if is_staff:
            if not empresa.prestadora_servico:
                raise serializers.ValidationError("Não é possível salvar um usuário 'is_staff=true' se a empresa "
                                      "vinculada não estiver como 'prestadora_servico=false'")

        if not is_staff:
            if empresa.prestadora_servico:
                raise serializers.ValidationError("Não é possível salvar um usuário 'is_staff=false' se a empresa "
                                      "vinculada estiver como 'prestadora_servico=true'")

        return is_staff

    def validate_empresa(self, empresa):
        usuario = self.initial_data
        is_staff = usuario['is_staff'] if 'is_staff' in usuario else False

        if not empresa.ativo:
            raise serializers.ValidationError("Não é possível salvar um usuário se a empresa vinculada está como "
                                              "'ativo=false'")

        if empresa.prestadora_servico:
            if not is_staff:
                raise serializers.ValidationError("Não é possível salvar um usuário 'is_staff=false' se a empresa "
                                                  "vinculada não estiver como 'prestadora_servico=true'")

        if not empresa.prestadora_servico:
            if is_staff:
                raise serializers.ValidationError("Não é possível salvar um usuário 'is_staff=true' se a empresa "
                                                  "vinculada estiver como 'prestadora_servico=false'")

        return empresa

    def validate_classificacao(self, classificacao):
        if not classificacao.ativo:
            raise serializers.ValidationError("Não é possível salvar um usuário se a classificação vinculada está como "
                                              "'ativo=false'")

        return classificacao

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError("Sua senha deve ter no mínimo 6 caracteres")

        if not re.findall('[A-Z]', password) or not re.findall('[a-z]', password) or not re.findall('[0-9]', password):
            raise serializers.ValidationError("A senha deve ser composta por letras, números e ao menos uma letra em "
                                              "caixa alta")

        return make_password(password)

    class Meta:
        model = Usuario
        read_only_fields = [
            'id',
            'last_login',
            'media_avaliacoes',
            'is_superuser',
            'is_staff',
            'is_manager',
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
            'id',
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
            'classificacao',
            'is_staff',
            'is_manager',
            'is_superuser',
            'is_active',
            'groups',
        ]


class UsuarioSerializerCreate(UsuarioSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True)
    classificacao = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                 required=False)

    class Meta(UsuarioSerializer.Meta):
        read_only_fields = [
            'id',
            'last_login',
            'media_avaliacoes',
        ]
        extra_kwargs = {
            'codigo_verificacao_segunda_etapa': {'write_only': True},
            'is_staff': {'allow_null': False},
        }


class UsuarioSerializerUpdatePartialUpdate(UsuarioSerializer):
    empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id')
    groups = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='id', many=True)
    classificacao = serializers.SlugRelatedField(queryset=Classificacao.objects.all(), slug_field='id',
                                                 required=False)

    class Meta(UsuarioSerializer.Meta):
        read_only_fields = [
            'id',
            'last_login',
            'media_avaliacoes',
            'username',
            'is_staff',
            'is_superuser',
            'empresa',
        ]


class UsuarioSerializerSimples(UsuarioSerializer):
    empresa = serializers.SlugRelatedField(read_only=True, slug_field='id')
    groups = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
    classificacao = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta(UsuarioSerializer.Meta):
        fields = [
            'id',
            'username',
            'email',
            'empresa',
            'classificacao',
            'is_staff',
            'is_manager',
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
    empresa = EmpresaSerializer(read_only=True)
    groups = GrupoPermissoesUsuarioSerializer(read_only=True, many=True)
    classificacao = ClassificacaoSerializer(read_only=True)
