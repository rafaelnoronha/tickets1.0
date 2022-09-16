from rest_framework.routers import SimpleRouter
from .views import AgrupamentoViewSet

router_agrupamento = SimpleRouter()
router_agrupamento.register('', AgrupamentoViewSet)
