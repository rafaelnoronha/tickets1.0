from rest_framework import serializers
from .models import Agrupamento


class AgrupamentoSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = Agrupamento
        fields = '__all__'


class AgrupamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agrupamento
        read_only_fields = [
            'id',
        ]
        extra_kwargs = {
            'codigo': {'allow_blank': True, },
        }
        fields = [
            'id',
            'codigo',
            'nome',
            'prioridade',
            'tipo',
            'ativo',
            'data_cadastro',
            'hora_cadastro',
        ]
