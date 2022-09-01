from rest_framework import serializers
from .models import Empresa


class EmpresaSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        read_only_fields = [
            'id',
            'codigo',
            'media_avaliacoes',
            'data_cadastro',
            'hora_cadastro',
        ]
        extra_kwargs = {
            'complemento': {'allow_blank': True},
        }
        fields = [
            'id',
            'codigo',
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
            'data_cadastro',
            'hora_cadastro',
        ]


class EmpresaSerializerUpdatePartialUpdate(EmpresaSerializer):
    class Meta(EmpresaSerializer.Meta):
        read_only_fields = [
            'id',
            'codigo',
            'media_avaliacoes',
            'data_cadastro',
            'hora_cadastro',
            'cpf_cnpj',
            'prestadora_servico',
            'data_cadastro',
            'hora_cadastro',
        ]
