class RegexTelefone:
    @staticmethod
    def get_regex():
        return r'\d{10}'

    @staticmethod
    def get_mensagem():
        return 'Informe um número de telefone válido. Ex: 3100000000'


class RegexCelular:
    @staticmethod
    def get_regex():
        return r'\d{2}9\{8}'

    @staticmethod
    def get_mensagem():
        return 'Informe um número de celular válido. Ex: 3190000000'


class RegexCodigoVerificacaoSegundaEtapa:
    @staticmethod
    def get_regex():
        return fr'\d{4}'

    @staticmethod
    def get_mensagem():
        return f'Certifique-se de que o campo tenha 4 caracteres numéricos'


class RegexCep:
    @staticmethod
    def get_regex():
        return fr'\d{8}'

    @staticmethod
    def get_mensagem():
        return f'Certifique-se de que o campo tenha 8 caracteres numéricos'
