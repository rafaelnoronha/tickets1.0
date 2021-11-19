from rest_framework import serializers
from .models import Usuario, LogAutenticacao


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class LogAutenticacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAutenticacao
        fields = '__all__'