from rest_framework import serializers
from .models import PrestadoraServico


class PrestadoraServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrestadoraServico
        fields = '__all__'
