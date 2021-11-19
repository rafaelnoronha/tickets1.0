from rest_framework.routers import SimpleRouter
from .views import UsuarioViewSet, LogAutenticacaoViewSet

router_usuario = SimpleRouter()
router_usuario.register('', UsuarioViewSet)

router_log_autenticacao = SimpleRouter()
router_log_autenticacao.register('', LogAutenticacaoViewSet)
