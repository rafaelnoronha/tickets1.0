from rest_framework import viewsets, mixins
from core.views import CreateModelMixinAuditoria, DestroyModelMixinAuditoria
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from .filters import PoliticaPrivacidadeFilter, ConsentimentoPoliticaPrivacidadeFilter
from core.permissions import BasePemission
from .serializer import (
    PoliticaPrivacidadeSerializer, ConsentimentoPoliticaPrivacidadeSerializer, ConsentimentoPoliticaPrivacidadeSerializerRetrieve,
    ConsentimentoPoliticaPrivacidadeSerializerCreate, PoliticaPrivacidadeSerializerAuditoria, ConsentimentoPliticaPrivacidadeSerializerAuditoria
)


class PoliticaPrivacidadeViewSet(
    CreateModelMixinAuditoria, mixins.RetrieveModelMixin, DestroyModelMixinAuditoria, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = PoliticaPrivacidade.objects.all()
    filterset_class = PoliticaPrivacidadeFilter
    permission_classes = (BasePemission, )
    serializer_class = PoliticaPrivacidadeSerializer
    auditoria = {
        'modelo': PoliticaPrivacidade,
        'nome_tabela': 'politica_privacidade',
        'serializer': PoliticaPrivacidadeSerializerAuditoria,
    }


class ConsentimentoPoliticaPrivacidadeViewSet(
    CreateModelMixinAuditoria, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = ConsentimentoPoliticaPrivacidade.objects \
        .prefetch_related('titular') \
        .prefetch_related('politica_privacidade') \
        .all()
    filterset_class = ConsentimentoPoliticaPrivacidadeFilter
    permission_classes = (BasePemission, )
    auditoria = {
        'modelo': ConsentimentoPoliticaPrivacidade,
        'nome_tabela': 'consentimento_politica_privacidade',
        'serializer': ConsentimentoPliticaPrivacidadeSerializerAuditoria,
    }

    serializer_classes = {
        'retrieve': ConsentimentoPoliticaPrivacidadeSerializerRetrieve,
        'create': ConsentimentoPoliticaPrivacidadeSerializerCreate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, ConsentimentoPoliticaPrivacidadeSerializer)
