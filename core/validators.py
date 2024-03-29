from django.core.exceptions import ValidationError
from django.core import validators
import functools
import re


class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = (
        'Digite um nome de usuário válido. Este valor pode conter apenas letras, '
        'números e caracteres @/./+/-/_.'
    )
    flags = 0


class RegexTelefone:
    @staticmethod
    def get_regex():
        return r'\d{10}'

    @staticmethod
    def get_mensagem():
        return 'Informe um número de telefone válido. Ex: 3100000000.'


class RegexCelular:
    @staticmethod
    def get_regex():
        return r'\d{2}9\d{8}'

    @staticmethod
    def get_mensagem():
        return 'Informe um número de celular válido. Ex: 31900000000.'


class RegexCodigoVerificacaoSegundaEtapa:
    @staticmethod
    def get_regex():
        return r'\d{4}'

    @staticmethod
    def get_mensagem():
        return 'Certifique-se de que o campo tenha 4 caracteres numéricos.'


class RegexCep:
    @staticmethod
    def get_regex():
        return r'\d{8}'

    @staticmethod
    def get_mensagem():
        return 'Certifique-se de que o campo tenha 8 caracteres numéricos.'


class ValidaCpfCnpj:
    @staticmethod
    def _calcular_digito_verificador_cpf_cnpj(array_cpf_cnpj, array_validador_cpf_cnpj):
        resultado_operacao = functools.reduce(
            lambda acumulador, digito_validador:
                acumulador + (digito_validador[1] * array_cpf_cnpj[digito_validador[0]])
            , enumerate(array_validador_cpf_cnpj), 0
        ) % 11

        return 11 - resultado_operacao if resultado_operacao in range(2, 11) else 0

    @staticmethod
    def valida_cpf(cpf_informado):
        cpf = list(map(lambda digito_cpf: int(digito_cpf), re.sub(r'\D', '', cpf_informado)))
        array_validador = [10, 9, 8, 7, 6, 5, 4, 3, 2]

        if len(cpf) != 11:
            raise ValidationError('Certifique-se de que o CPF tenha 11 dígitos.')

        if re.findall(r'0{11}|1{11}|2{11}|3{11}|4{11}|5{11}|6{11}|7{11}|8{11}|9{11}', functools.reduce(
                        lambda acumulador, digito_cpf: acumulador + str(digito_cpf), cpf, '')
                      ):
            raise ValidationError('O CPF informado é inválido.')

        primeiro_digito_verificador = ValidaCpfCnpj._calcular_digito_verificador_cpf_cnpj(cpf, array_validador)
        array_validador.insert(0, 11)
        segundo_digito_verificador = ValidaCpfCnpj._calcular_digito_verificador_cpf_cnpj(cpf, array_validador)

        cpf_validado = cpf[0:9].copy()
        cpf_validado.append(primeiro_digito_verificador)
        cpf_validado.append(segundo_digito_verificador)

        if cpf != cpf_validado:
            raise ValidationError('O CPF informado é inválido.')

    @staticmethod
    def valida_cnpj(cnpj_informado):
        cnpj = list(map(lambda digito_cnpj: int(digito_cnpj), re.sub(r'\D', '', cnpj_informado)))
        array_validador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        if len(cnpj) != 14:
            raise ValidationError('Certifique-se de que o CNPJ tenha 14 dígitos.')

        if re.findall(r'0{14}|1{14}|2{14}|3{14}|4{14}|5{14}|6{14}|7{14}|8{14}|9{14}', functools.reduce(
                        lambda acumulador, digito_cpf: acumulador + str(digito_cpf), cnpj, '')
                      ):
            raise ValidationError('O CNPJ informado é inválido.')

        primeiro_digito_verificador = ValidaCpfCnpj._calcular_digito_verificador_cpf_cnpj(cnpj, array_validador)
        array_validador.insert(0, 6)
        segundo_digito_verificador = ValidaCpfCnpj._calcular_digito_verificador_cpf_cnpj(cnpj, array_validador)

        cnpj_validado = cnpj[0:12].copy()
        cnpj_validado.append(primeiro_digito_verificador)
        cnpj_validado.append(segundo_digito_verificador)

        if cnpj != cnpj_validado:
            raise ValidationError('O CNPJ informado é inválido.')

    @staticmethod
    def valida_cpf_cnpj(cpf_cnpj):
        if len(cpf_cnpj) == 11:
            return ValidaCpfCnpj.valida_cpf(cpf_cnpj)
        elif len(cpf_cnpj) == 14:
            return ValidaCpfCnpj.valida_cnpj(cpf_cnpj)

        raise ValidationError('Informe 11 dígitos para CPF ou 14 para CNPJ.')
