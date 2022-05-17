from rest_framework import serializers
from .models import Empresa


class EmpresaSerializerAuditoria(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    def validate_prestadora_servico(self, prestadora_servico):
        empresa = self.instance
        empresa_requisicao = self.initial_data
        empresa_prestadora_servico = Empresa.objects.filter(prestadora_servico=True)

        if prestadora_servico:
            if not empresa_prestadora_servico:
                return prestadora_servico

            if len(empresa_prestadora_servico) > 1:
                raise serializers.ValidationError("Não é permitido mais de um cadastro de empresa como "
                                                  "'prestadora_servico=true'")

            if empresa and empresa_prestadora_servico[0].uuid != empresa.uuid:
                raise serializers.ValidationError("Não é permitido mais de um cadastro de empresa como "
                                                  "'prestadora_servico=true'")

            if empresa_prestadora_servico[0].cpf_cnpj != empresa_requisicao['cpf_cnpj']:
                raise serializers.ValidationError("Não é permitido mais de um cadastro de empresa como "
                                                  "'prestadora_servico=true'")

        return prestadora_servico

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
            'data_cadastro',
            'hora_cadastro',
        ]
