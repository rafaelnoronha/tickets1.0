from rest_framework import serializers
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from usuario.models import Usuario
from usuario.serializer import UsuarioSerializerSimples
from datetime import date


class PoliticaPrivacidadeSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = PoliticaPrivacidade
        fields = '__all__'


class ConsentimentoPliticaPrivacidadeSerializerAuditoria(serializers.ModelSerializer):
    titular = serializers.SlugRelatedField(read_only=True, slug_field='id')
    politica_privacidade = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = ConsentimentoPoliticaPrivacidade
        fields = '__all__'


class PoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    def validate_data_validade(self, data_validade):
        if data_validade < date.today():
            raise serializers.ValidationError('A data de validade não pode ser maior que a data atual')

        return data_validade

    class Meta:
        model = PoliticaPrivacidade
        read_only_fields = [
            'id',
            'data_cadastro',
            'hora_cadastro',
        ]
        fields = [
            'id',
            'codigo',
            'titulo',
            'descricao',
            'tipo_titular',
            'data_validade',
            'ativo',
            'data_cadastro',
            'hora_cadastro',
        ]


class ConsentimentoPoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    titular = serializers.SlugRelatedField(read_only=True, slug_field='username')
    politica_privacidade = serializers.SlugRelatedField(read_only=True, slug_field='titulo')

    def validate_politica_privacidade(self, politica_privacidade):
        if politica_privacidade.data_validade < date.today():
            raise serializers.ValidationError('Não é possível consentir com uma política de privacidade vencida')

        if not politica_privacidade.ativo:
            raise serializers.ValidationError("Não é possível consentir com uma política de privacidade inativa")

        return politica_privacidade

    def validate_titular(self, titular):
        if not titular.is_active:
            raise serializers.ValidationError("Não é possível consentir com uma política de privacidade com o titular "
                                              "inativo")

        return titular

    class Meta:
        model = ConsentimentoPoliticaPrivacidade
        read_only_fields = [
            'id',
            'data_cadastro',
            'hora_cadastro',
        ]
        fields = [
            'id',
            'titular',
            'politica_privacidade',
            'consentimento',
            'data_cadastro',
            'hora_cadastro',
        ]


class ConsentimentoPoliticaPrivacidadeSerializerRetrieve(ConsentimentoPoliticaPrivacidadeSerializer):
    titular = UsuarioSerializerSimples(read_only=True)
    politica_privacidade = PoliticaPrivacidadeSerializer(read_only=True)


class ConsentimentoPoliticaPrivacidadeSerializerCreate(ConsentimentoPoliticaPrivacidadeSerializer):
    titular = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id')
    politica_privacidade = serializers.SlugRelatedField(queryset=PoliticaPrivacidade.objects.all(), slug_field='id')
