from rest_framework import serializers
from .models import Usuario, LogAutenticacao
from empresa.models import Empresa


class UsuarioSerializer(serializers.ModelSerializer):
    empresa = serializers.HyperlinkedRelatedField(
        many=False,
        allow_null=True,
        view_name='empresa-detail',
        queryset=Empresa.objects.all()
    )

    class Meta:
        model = Usuario
        read_only_fields = [
            'uuid',
            'last_login',
            'date_joined',
            'media_avaliacoes',
            'numero_tentativas_login',
            'verificacao_duas_etapas',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'codigo_verificacao_segunda_etapa': {'write_only': True},
            'empresa': {'write_only': True},
            'first_name': {'allow_null': False, 'allow_blank': False},
            'last_name': {'allow_null': False, 'allow_blank': False},
            'email': {'allow_null': False, 'allow_blank': False},
        }
        fields = [
            'uuid',
            'date_joined',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'telefone',
            'celular',
            'observacoes',
            'media_avaliacoes',
            'empresa',
            'last_login',
            'numero_tentativas_login',
            'verificacao_duas_etapas',
            'codigo_verificacao_segunda_etapa',
            'is_superuser',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
        ]


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
