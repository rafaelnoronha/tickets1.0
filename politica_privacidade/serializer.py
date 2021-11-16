from rest_framework import serializers
from .models import PoliticaPrivacidade


class PoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticaPrivacidade
        fields = '__all__'
