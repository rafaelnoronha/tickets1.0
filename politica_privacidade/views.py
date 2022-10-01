from rest_framework import viewsets, mixins
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from .filters import PoliticaPrivacidadeFilter, ConsentimentoPoliticaPrivacidadeFilter
from core.permissions import BasePemission
from .serializer import (
    PoliticaPrivacidadeSerializer, ConsentimentoPoliticaPrivacidadeSerializer, ConsentimentoPoliticaPrivacidadeSerializerRetrieve,
    ConsentimentoPoliticaPrivacidadeSerializerCreate
)


class PoliticaPrivacidadeViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = PoliticaPrivacidade.objects.all()
    filterset_class = PoliticaPrivacidadeFilter
    permission_classes = (BasePemission, )
    serializer_class = PoliticaPrivacidadeSerializer


class ConsentimentoPoliticaPrivacidadeViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = ConsentimentoPoliticaPrivacidade.objects.all() \
        .prefetch_related('titular') \
        .prefetch_related('politica_privacidade')
    filterset_class = ConsentimentoPoliticaPrivacidadeFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'retrieve': ConsentimentoPoliticaPrivacidadeSerializerRetrieve,
        'create': ConsentimentoPoliticaPrivacidadeSerializerCreate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, ConsentimentoPoliticaPrivacidadeSerializer)
