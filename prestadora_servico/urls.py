from rest_framework.routers import SimpleRouter
from .views import PrestadoraServicoViewSet

router_prestadora_servico = SimpleRouter()
router_prestadora_servico.register('', PrestadoraServicoViewSet)
