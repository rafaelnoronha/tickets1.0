from rest_framework import serializers
from .models import Agrupamento, Classificacao


class AgrupamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agrupamento
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
        read_only_fields = [
            'id',
        ]
        extra_kwargs = {
            'gr_codigo': {'allow_blank': True, },
        }


class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao
        fields = [
            'id',
            'codigo',
            'nome',
            'descricao',
            'ativo',
        ]
        read_only_fields = [
            'id',
            'data_cadastro',
            'hora_cadastro',
        ]
