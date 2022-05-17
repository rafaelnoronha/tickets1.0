from rest_framework import serializers
from .models import Grupo, Subgrupo


class GrupoSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'


class SubgrupoSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = Subgrupo
        fields = '__all__'


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        read_only_fields = [
            'uuid',
        ]
        extra_kwargs = {
            'codigo': {'allow_blank': True, },
            'peso': {'allow_null': True, },
        }
        fields = [
            'uuid',
            'codigo',
            'nome',
            'peso',
            'tipo',
            'ativo',
            'data_cadastro',
            'hora_cadastro',
        ]


class SubgrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgrupo
        read_only_fields = [
            'uuid',
        ]
        extra_kwargs = {
            'codigo': {'allow_blank': True, },
            'peso': {'allow_null': True, },
        }
        fields = [
            'uuid',
            'codigo',
            'nome',
            'peso',
            'tipo',
            'ativo',
            'data_cadastro',
            'hora_cadastro',
        ]
