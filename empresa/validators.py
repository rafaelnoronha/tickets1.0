from django.core.exceptions import ValidationError
from . import models


class EmpresaValidator:
    @staticmethod
    def valida_prestadora_servico(prestadora_servico):
        if prestadora_servico and models.Empresa.objects.filter(prestadora_servico=True, ativo=True):
            raise ValidationError('Já existe uma empresa prestadora de serviço ativa')
