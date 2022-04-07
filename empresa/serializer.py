from rest_framework import serializers
from .models import Empresa


class EmpresaSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa

        extra_kwargs = {
            'complemento': {'allow_blank': True},
        }

        read_only_fields = [
            'uuid',
            'media_avaliacoes',
        ]

        fields = [
            'uuid',
            'cpf_cnpj',
            'razao_social',
            'nome_fantasia',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'municipio',
            'uf',
            'cep',
            'pais',
            'telefone',
            'media_avaliacoes',
            'prestadora_servico',
            'ativo',
        ]
