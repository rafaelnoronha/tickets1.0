from rest_framework import serializers
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from usuario.models import Usuario
from usuario.serializer import UsuarioSerializerSimples
from datetime import date


class PoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    def validate_data_validade(self, pl_data_validade):
        if pl_data_validade < date.today():
            raise serializers.ValidationError('A data de validade não pode ser maior que a data atual')

        return pl_data_validade

    class Meta:
        model = PoliticaPrivacidade
        fields = [
            'id',
            'pl_codigo',
            'pl_titulo',
            'pl_descricao',
            'pl_tipo_titular',
            'pl_data_validade',
            'ativo',
            'data_cadastro',
            'hora_cadastro',
        ]
        read_only_fields = [
            'id',
            'data_cadastro',
            'hora_cadastro',
        ]


class ConsentimentoPoliticaPrivacidadeSerializer(serializers.ModelSerializer):
    cn_titular = serializers.SlugRelatedField(read_only=True, slug_field='username')
    cn_politica_privacidade = serializers.SlugRelatedField(read_only=True, slug_field='pl_titulo')

    def validate_politica_privacidade(self, cn_politica_privacidade):
        if cn_politica_privacidade.pl_data_validade < date.today():
            raise serializers.ValidationError('Não é possível consentir com uma política de privacidade vencida')

        if not cn_politica_privacidade.ativo:
            raise serializers.ValidationError("Não é possível consentir com uma política de privacidade inativa")

        return cn_politica_privacidade

    def validate_titular(self, titular):
        if not titular.is_active:
            raise serializers.ValidationError("Não é possível consentir com uma política de privacidade com o titular inativo")

        return titular

    class Meta:
        model = ConsentimentoPoliticaPrivacidade
        fields = [
            'id',
            'cn_titular',
            'cn_politica_privacidade',
            'cn_consentimento',
            'data_cadastro',
            'hora_cadastro',
        ]
        read_only_fields = [
            'id',
            'data_cadastro',
            'hora_cadastro',
        ]


class ConsentimentoPoliticaPrivacidadeSerializerRetrieve(ConsentimentoPoliticaPrivacidadeSerializer):
    cn_titular = UsuarioSerializerSimples(read_only=True)
    cn_politica_privacidade = PoliticaPrivacidadeSerializer(read_only=True)


class ConsentimentoPoliticaPrivacidadeSerializerCreate(ConsentimentoPoliticaPrivacidadeSerializer):
    cn_titular = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='id')
    cn_politica_privacidade = serializers.SlugRelatedField(queryset=PoliticaPrivacidade.objects.all(), slug_field='id')
