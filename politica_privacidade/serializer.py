from rest_framework import serializers
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from usuario.models import Usuario
from usuario.serializer import UsuarioSerializer


class PoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticaPrivacidade
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'uuid',
            'titulo_politica',
            'politica',
            'tipo_titular',
            'data_validade',
            'ativo',
        ]


class ConsentimentoPoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    titular = serializers.SlugRelatedField(read_only=True, slug_field='username')
    politica_privacidade = serializers.SlugRelatedField(read_only=True, slug_field='titulo_politica')

    class Meta:
        model = ConsentimentoPoliticaPrivacidade
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'uuid',
            'titular',
            'politica_privacidade',
            'consentimento',
        ]


class ConsentimentoPoliticaPrivacidadeSerializerRetrieve(ConsentimentoPoliticaPrivacidadeSerializer):
    titular = UsuarioSerializer(read_only=True)
    politica_privacidade = PoliticaPrivacidadeSerializer(read_only=True)


class ConsentimentoPoliticaPrivacidadeSerializerCreate(ConsentimentoPoliticaPrivacidadeSerializer):
    titular = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    politica_privacidade = serializers.PrimaryKeyRelatedField(queryset=PoliticaPrivacidade.objects.all())
