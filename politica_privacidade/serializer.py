from rest_framework import serializers
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from usuario.models import Usuario
from usuario.serializer import UsuarioSerializerSimples


class PoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticaPrivacidade
        read_only_fields = [
            'uuid',
        ]
        fields = [
            'uuid',
            'titulo',
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
    titular = UsuarioSerializerSimples(read_only=True)
    politica_privacidade = PoliticaPrivacidadeSerializer(read_only=True)


class ConsentimentoPoliticaPrivacidadeSerializerCreate(ConsentimentoPoliticaPrivacidadeSerializer):
    titular = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='uuid')
    politica_privacidade = serializers.SlugRelatedField(queryset=PoliticaPrivacidade.objects.all(), slug_field='uuid')
