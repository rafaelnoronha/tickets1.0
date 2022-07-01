from rest_framework.routers import SimpleRouter
from .views import TicketViewSet, MensagemTicketViewSet, MovimentoTicketViewSet

router_ticket = SimpleRouter()
router_ticket.register('', TicketViewSet)

router_mensagem_ticket = SimpleRouter()
router_mensagem_ticket.register('', MensagemTicketViewSet)

router_movimento_ticket = SimpleRouter()
router_movimento_ticket.register('', MovimentoTicketViewSet)
