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
    def valida_cpf(cpf_informado):
        cpf = list(map(lambda item_lista: int(item_lista), re.sub(r'\D', '', cpf_informado)))

        if len(cpf) != 11:
            raise ValidationError('Certifique-se de que o cpf tenha 11 números.')

        cpf_validado = cpf[0:9]

        operacao_primeiro_digito_verificador = functools.reduce(
            lambda acumulador, digito_cpf:
                acumulador + (digito_cpf * (cpf[0:9].index(digito_cpf) + 1))
            , cpf[0:9]) % 11

        primeiro_digito_verificador = operacao_primeiro_digito_verificador \
            if operacao_primeiro_digito_verificador >= 10 else 0

        cpf_validado.append(primeiro_digito_verificador)

        operacao_segundo_digito_verificador = functools.reduce(
            lambda acumulador, digito_cpf:
            acumulador + (digito_cpf * cpf_validado.index(digito_cpf))
            , cpf_validado) % 11

        segundo_digito_verificador = operacao_segundo_digito_verificador \
            if operacao_segundo_digito_verificador >= 10 else 0

        print(primeiro_digito_verificador)
        print(segundo_digito_verificador)
