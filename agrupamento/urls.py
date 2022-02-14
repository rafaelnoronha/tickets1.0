from rest_framework.routers import SimpleRouter
from .views import GrupoViewSet, SubgrupoViewSet

router_grupo = SimpleRouter()
router_grupo.register('', GrupoViewSet)

router_subgrupo = SimpleRouter()
router_subgrupo.register('', SubgrupoViewSet)
