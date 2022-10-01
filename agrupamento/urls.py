from rest_framework.routers import SimpleRouter
from .views import AgrupamentoViewSet, ClassificacaoViewSet

router_agrupamento = SimpleRouter()
router_agrupamento.register('', AgrupamentoViewSet)

router_classificacao = SimpleRouter()
router_classificacao.register('', ClassificacaoViewSet)
