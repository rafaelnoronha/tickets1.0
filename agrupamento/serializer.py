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
            'gr_codigo': {'allow_blank': True, },
        }
        fields = [
            'id',
            'gr_codigo',
            'gr_nome',
            'gr_prioridade',
            'gr_tipo',
            'ativo',
            'data_cadastro',
            'hora_cadastro',
        ]
