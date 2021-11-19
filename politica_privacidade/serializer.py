from rest_framework import serializers
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade


class PoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticaPrivacidade
        fields = '__all__'


class ConsentimentoPoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsentimentoPoliticaPrivacidade
        fields = '__all__'
