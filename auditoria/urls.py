from rest_framework.routers import SimpleRouter
from .views import AuditoriaViewSet, LogAutenticacaoViewSet

router_auditoria = SimpleRouter()
router_auditoria.register('', AuditoriaViewSet)

router_log_autenticacao = SimpleRouter()
router_log_autenticacao.register('', LogAutenticacaoViewSet)
