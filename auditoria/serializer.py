from rest_framework import serializers
from .models import Auditoria
from usuario.serializer import UsuarioSerializerSimples


class AuditoriaSerializer(serializers.ModelSerializer):
    usuario_operacao = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Auditoria
        read_only_fields = [
            'id',
            'dt_data_operacao',
            'dt_hora_operacao',
            'dt_tabela_operacao',
            'dt_tipo_operacao',
            'dt_usuario_operacao',
            'dt_estado_anterior',
            'dt_estado_atual',
        ]
        fields = [
            'id',
            'dt_data_operacao',
            'dt_hora_operacao',
            'dt_tabela_operacao',
            'dt_tipo_operacao',
            'dt_usuario_operacao',
            'dt_estado_anterior',
            'dt_estado_atual',
        ]


class AuditoriaSerializerRetrieve(AuditoriaSerializer):
    usuario_operacao = UsuarioSerializerSimples(read_only=True)


class LogAutenticacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = LogAutenticacao
        read_only_fields = ['id']
        fields = [
            'id',
            'ip',
            'autenticado',
            'data_autenticacao',
            'hora_autenticacao',
            'usuario',
        ]


class LogAutenticacaoSerializerRetrieve(LogAutenticacaoSerializer):
    usuario = UsuarioSerializerSimples(read_only=True)
