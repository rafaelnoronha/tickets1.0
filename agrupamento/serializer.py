from rest_framework import serializers
from .models import Grupo, Subgrupo


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
        ]
