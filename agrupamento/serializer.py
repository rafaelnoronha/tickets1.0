from rest_framework import serializers
from .models import Grupo, Subgrupo


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        read_only_fields = [
            'uuid',
        ]
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
        fields = [
            'uuid',
            'codigo',
            'nome',
            'peso',
            'tipo',
        ]
