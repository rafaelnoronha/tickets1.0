from rest_framework import serializers
from .models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id',
            'mp_cpf_cnpj',
            'mp_razao_social',
            'mp_nome_fantasia',
            'mp_logradouro',
            'mp_numero',
            'mp_complemento',
            'mp_bairro',
            'mp_municipio',
            'mp_uf',
            'mp_cep',
            'mp_pais',
            'mp_telefone',
            'mp_media_avaliacoes',
            'mp_prestadora_servico',
            'ativo',
            'data_cadastro',
            'hora_cadastro',
        ]
        read_only_fields = [
            'id',
            'mp_media_avaliacoes',
            'mp_data_cadastro',
            'mp_hora_cadastro',
        ]
        extra_kwargs = {
            'complemento': {'allow_blank': True},
        }


class EmpresaSerializerUpdatePartialUpdate(EmpresaSerializer):
    class Meta(EmpresaSerializer.Meta):
        read_only_fields = [
            'id',
            'mp_media_avaliacoes',
            'mp_data_cadastro',
            'mp_hora_cadastro',
            'mp_cpf_cnpj',
            'mp_prestadora_servico',
            'data_cadastro',
            'hora_cadastro',
        ]
