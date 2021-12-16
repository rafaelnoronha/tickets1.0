from django.core.exceptions import ValidationError
import functools
import re


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
        return r'\d{2}9\{8}'

    @staticmethod
    def get_mensagem():
        return 'Informe um número de celular válido. Ex: 3190000000.'


class RegexCodigoVerificacaoSegundaEtapa:
    @staticmethod
    def get_regex():
        return fr'\d{4}'

    @staticmethod
    def get_mensagem():
        return f'Certifique-se de que o campo tenha 4 caracteres numéricos.'


class RegexCep:
    @staticmethod
    def get_regex():
        return fr'\d{8}'

    @staticmethod
    def get_mensagem():
        return f'Certifique-se de que o campo tenha 8 caracteres numéricos.'


class ValidaCpfCnpj:
    @staticmethod
    def _calcular_digito_verificador(array_cpf):
        resultado_operacao = functools.reduce(
            lambda acumulador, digito_cpf:
                acumulador + ((digito_cpf[0] + 2) * digito_cpf[1])
            , enumerate(array_cpf), 0) % 11

        return 11 - resultado_operacao if resultado_operacao >= 2 else 0

    @staticmethod
    def valida_cpf(cpf_informado):
        cpf = list(map(lambda item_lista: int(item_lista), re.sub(r'\D', '', cpf_informado)))

        if len(cpf) != 11:
            raise ValidationError('Certifique-se de que o cpf tenha 11 números.')

        if re.findall(r'0{11}|1{11}|2{11}|3{11}|4{11}|5{11}|6{11}|7{11}|8{11}|9{11}', functools.reduce(
                        lambda acumulador, digito_cpf: acumulador + str(digito_cpf), cpf, '')
                      ):
            raise ValidationError('O CPF informado é inválido.')

        cpf_validado = cpf[0:9].copy()
        cpf_validado.reverse()

        primeiro_digito_verificador = ValidaCpfCnpj._calcular_digito_verificador(cpf_validado)
        cpf_validado.insert(0, primeiro_digito_verificador)

        segundo_digito_verificador = ValidaCpfCnpj._calcular_digito_verificador(cpf_validado)
        cpf_validado.insert(0, segundo_digito_verificador)

        cpf_validado.reverse()

        if cpf != cpf_validado:
            raise ValidationError('O CPF informado é inválido.')
