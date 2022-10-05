from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.db import connection
from .models import Ticket, MensagemTicket, MovimentoTicket
from .filters import TicketFilter, MensagemTicketFilter, MovimentoTicketFilter
from core.permissions import BasePemission
from .serializer import TicketSerializer, TicketSerializerRetrieve, TicketSerializerCreate, \
                        TicketSerializerUpdatePartialUpdate, MensagemTicketSerializer, MensagemTicketSerializerCreate, \
                        MensagemTicketSerializerRetrieve, \
                        TicketSerializerAvaliar, TicketSerializerAtribuirAtendente, TicketSerializerReclassificar, \
                        MovimentoTicketSerializer, MovimentoTicketSerializerRetrieve
                        # TicketSerializerFinalizar, TicketSerializerCancelar, TicketSerializerSolucionar, \


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all() \
        .prefetch_related('tc_solicitante') \
        .prefetch_related('tc_classificacao_atendente') \
        .prefetch_related('tc_atendente') \
        .prefetch_related('tc_grupo') \
        .prefetch_related('tc_subgrupo')
    filterset_class = TicketFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'retrieve': TicketSerializerRetrieve,
        'create': TicketSerializerCreate,
        'update': TicketSerializerUpdatePartialUpdate,
        'partial_update': TicketSerializerUpdatePartialUpdate,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, TicketSerializer)

    def get_queryset(self):
        queryset = Ticket.objects \
            .prefetch_related('tc_solicitante') \
            .prefetch_related('tc_classificacao_atendente') \
            .prefetch_related('tc_atendente') \
            .prefetch_related('tc_grupo') \
            .prefetch_related('tc_subgrupo')
        usuario = self.request.user

        if usuario.is_superuser:
            return self.queryset

        if usuario.is_staff:
            if not usuario.sr_is_manager:
                return queryset.filter(Q(tc_atendente=usuario) | Q(tc_atendente__isnull=True))

            return queryset.filter(Q(tc_atendente__empresa=usuario.empresa) | Q(tc_atendente__isnull=True))
        else:
            if usuario.is_manager:
                return queryset.filter(tc_solicitante__empresa=usuario.empresa)
            else:
                return queryset.filter(tc_solicitante=usuario)

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print(' QUERIES '.center(100, '='))
        print(f'Número de consultas { len(connection.queries) }')
        print('='*100)
        print(' CONSULTAS '.center(100, '='))
        for consulta in connection.queries:
            print(consulta)
            print()
        print('='*100)
        return response

    @action(detail=True, methods=['get'])
    def movimento(self, request, id):
        instance = self.get_object()
        movimentos = MovimentoTicket.objects.filter(ticket=instance)
        serializer = MovimentoTicketSerializer(movimentos, many=True)
        headers = self.get_success_headers(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def atribuir(self, request, id):
        instance = self.get_object()
        serializer = TicketSerializerAtribuirAtendente(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def reclassificar(self, request, id):
        instance = self.get_object()
        instance.atendente = None
        serializer = TicketSerializerReclassificar(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    # @action(detail=True, methods=['patch'])
    # def solucionar(self, request, id):
    #     instance = self.get_object()
    #     serializer = TicketSerializerSolucionar(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     headers = self.get_success_headers(serializer.data)

    #     return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    # @action(detail=True, methods=['patch'])
    # def finalizar(self, request, id):
    #     instance = self.get_object()
    #     serializer = TicketSerializerFinalizar(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     headers = self.get_success_headers(serializer.data)

    #     return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    @action(detail=True, methods=['patch'])
    def avaliar(self, request, id):
        instance = self.get_object()
        serializer = TicketSerializerAvaliar(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    # @action(detail=True, methods=['patch'])
    # def cancelar(self, request, id):
    #     instance = self.get_object()
    #     serializer = TicketSerializerCancelar(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     headers = self.get_success_headers(serializer.data)

    #     return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class MensagemTicketViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MensagemTicket.objects.all() \
        .prefetch_related('mn_usuario') \
        .prefetch_related('mn_ticket') \
        .prefetch_related('mn_mensagem_relacionada')
    filterset_class = MensagemTicketFilter
    permission_classes = (BasePemission, )

    serializer_classes = {
        'create': MensagemTicketSerializerCreate,
        'retrieve': MensagemTicketSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, MensagemTicketSerializer)

    def get_queryset(self):
        queryset = MensagemTicket.objects \
            .prefetch_related('mn_usuario') \
            .prefetch_related('mn_ticket') \
            .prefetch_related('mn_mensagem_relacionada')
        usuario = self.request.user

        if usuario.is_superuser:
            return self.queryset

        if usuario.is_staff:
            if not usuario.tc_is_manager:
                return queryset.filter(mn_ticket__atendente=usuario)

            return queryset.filter(mn_ticket__atendente__empresa=usuario.empresa)
        else:
            if usuario.is_manager:
                return queryset.filter(mn_ticket__solicitante__empresa=usuario.empresa)
            else:
                return queryset.filter(mn_ticket__solicitante=usuario)


class MovimentoTicketViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MovimentoTicket.objects.all() \
        .prefetch_related('mv_ticket') \
        .prefetch_related('mv_atendente') \
        .prefetch_related('mv_classificacao_atendente') \
        .prefetch_related('mv_solucionado') \
        .prefetch_related('mv_finalizado') \
        .prefetch_related('mv_cancelado')
    filterset_class = MovimentoTicketFilter
    permission_classes = (BasePemission,)

    serializer_classes = {
        'retrieve': MovimentoTicketSerializerRetrieve,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, MovimentoTicketSerializer)
