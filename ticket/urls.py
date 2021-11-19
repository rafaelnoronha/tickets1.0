from rest_framework.routers import SimpleRouter
from .views import TicketViewSet, MensagemTicketViewSet

router_ticket = SimpleRouter()
router_ticket.register('', TicketViewSet)

router_mensagem_ticket = SimpleRouter()
router_mensagem_ticket.register('', MensagemTicketViewSet)