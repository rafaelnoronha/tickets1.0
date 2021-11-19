from rest_framework.routers import SimpleRouter
from .views import EmpresaViewSet

router_empresa = SimpleRouter()
router_empresa.register('', EmpresaViewSet)
