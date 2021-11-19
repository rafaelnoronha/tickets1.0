from rest_framework.routers import SimpleRouter
from .views import PoliticaPrivacidadeViewSet, ConsentimentoPoliticaPrivacidadeViewSet

router_politica_privacidade = SimpleRouter()
router_politica_privacidade.register('', PoliticaPrivacidadeViewSet)

router_consentimento_politica_privacidade = SimpleRouter()
router_consentimento_politica_privacidade.register('', ConsentimentoPoliticaPrivacidadeViewSet)