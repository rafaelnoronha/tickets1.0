from rest_framework.routers import SimpleRouter
from .views import AuditoriaViewSet

router_auditoria = SimpleRouter()
router_auditoria.register('', AuditoriaViewSet)