from rest_framework.routers import SimpleRouter
from .views import UsuarioViewSet, GrupoPermissoesUsuarioViewSet,\
                    PermissaoUsuarioViewSet

router_usuario = SimpleRouter()
router_usuario.register('', UsuarioViewSet)

router_grupo_permissoes_usuario = SimpleRouter()
router_grupo_permissoes_usuario.register('', GrupoPermissoesUsuarioViewSet)

router_permissao_usuario = SimpleRouter()
router_permissao_usuario.register('', PermissaoUsuarioViewSet)
