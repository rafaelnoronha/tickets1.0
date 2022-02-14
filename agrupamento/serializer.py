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
            'nome',
            'peso',
        ]


class SubgrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgrupo
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'uuid',
            'nome',
            'peso',
        ]
