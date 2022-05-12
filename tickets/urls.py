"""tickets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuario.urls import router_usuario, router_log_autenticacao, router_grupo_permissoes_usuario, \
    router_permissao_usuario
from empresa.urls import router_empresa
from politica_privacidade.urls import router_politica_privacidade, router_consentimento_politica_privacidade
from ticket.urls import router_ticket, router_mensagem_ticket
from auditoria.urls import router_auditoria
from agrupamento.urls import router_grupo, router_subgrupo

base_url_v1 = 'api/v1/'

urlpatterns = [
    path(f'{base_url_v1}token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{base_url_v1}token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{base_url_v1}usuario', include(router_usuario.urls)),
    path(f'{base_url_v1}log_autenticacao', include(router_log_autenticacao.urls)),
    path(f'{base_url_v1}grupo_permissoes_usuario', include(router_grupo_permissoes_usuario.urls)),
    path(f'{base_url_v1}permissao_usuario', include(router_permissao_usuario.urls)),
    path(f'{base_url_v1}empresa', include(router_empresa.urls)),
    path(f'{base_url_v1}politica_privacidade', include(router_politica_privacidade.urls)),
    path(f'{base_url_v1}consentimento_politica_privacidade', include(router_consentimento_politica_privacidade.urls)),
    path(f'{base_url_v1}ticket', include(router_ticket.urls)),
    path(f'{base_url_v1}mensagem_ticket', include(router_mensagem_ticket.urls)),
    path(f'{base_url_v1}auditoria', include(router_auditoria.urls)),
    path(f'{base_url_v1}grupo', include(router_grupo.urls)),
    path(f'{base_url_v1}subgrupo', include(router_subgrupo.urls)),
]