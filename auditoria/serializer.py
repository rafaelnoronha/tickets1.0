from rest_framework import serializers
from .models import Auditoria
from usuario.serializer import UsuarioSerializerSimples


class AuditoriaSerializer(serializers.ModelSerializer):
    usuario_operacao = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Auditoria
        read_only_fields = [
            'id',
            'data_operacao',
            'hora_operacao',
            'tabela_operacao',
            'tipo_operacao',
            'usuario_operacao',
            'estado_anterior',
            'estado_atual',
        ]
        fields = [
            'id',
            'data_operacao',
            'hora_operacao',
            'tabela_operacao',
            'tipo_operacao',
            'usuario_operacao',
            'estado_anterior',
            'estado_atual',
        ]


class AuditoriaSerializerRetrieve(AuditoriaSerializer):
    usuario_operacao = UsuarioSerializerSimples(read_only=True)
