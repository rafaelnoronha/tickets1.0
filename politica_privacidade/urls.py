from rest_framework.routers import SimpleRouter
from .views import PoliticaPrivacidadeViewSet


router = SimpleRouter()
router.register('politica_privacidade', PoliticaPrivacidadeViewSet)
