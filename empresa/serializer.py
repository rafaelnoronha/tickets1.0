from rest_framework import serializers
from .models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa

        extra_kwargs = {
            'complemento': {'allow_blank': True},
        }

        read_only_fields = [
            'uuid',
            'prestadora_servico',
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
