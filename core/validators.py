from django.core.exceptions import ValidationError


def not_null_or_empty_validator(valor):
    if valor.isspace():
        raise ValidationError('%(valor)s não pode ser uma string vazia', params={'valor': valor})
