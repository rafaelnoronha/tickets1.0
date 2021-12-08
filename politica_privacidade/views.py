from rest_framework import viewsets, mixins
from .models import PoliticaPrivacidade, ConsentimentoPoliticaPrivacidade
from .serializer import PoliticaPrivacidadeSerializer, ConsentimentoPoliticaPrivacidadeSerializer, \
                        ConsentimentoPoliticaPrivacidadeSerializerRetrieve, \
                        ConsentimentoPoliticaPrivacidadeSerializerCreate


class PoliticaPrivacidadeViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                                 mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PoliticaPrivacidade.objects.all()
    lookup_field = 'uuid'
    serializer_class = PoliticaPrivacidadeSerializer


class ConsentimentoPoliticaPrivacidadeViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                                              viewsets.GenericViewSet):
    queryset = ConsentimentoPoliticaPrivacidade.objects.all()
    lookup_field = 'uuid'

    serializer_classes = {
        'retrieve': ConsentimentoPoliticaPrivacidadeSerializerRetrieve,
        'create': ConsentimentoPoliticaPrivacidadeSerializerCreate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, ConsentimentoPoliticaPrivacidadeSerializer)
