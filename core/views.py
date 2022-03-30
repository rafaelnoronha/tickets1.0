from rest_framework import viewsets, mixins
from auditoria.models import Auditoria
from usuario.models import Usuario
from rest_framework.response import Response
from rest_framework import status


class ModelViewSetComAuditoria(viewsets.ModelViewSet):
    nome_tabela_para_auditoria = None

    def update(self, request, *args, **kwargs):
        usuario_antes_da_alteracao = Usuario.objects.get(id=self.get_object().id)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        Auditoria.objects.create(tabela_operacao=self.nome_tabela_para_auditoria, tipo_operacao='UPDATE',
                                 usuario_operacao=request.user, estado_anterior=usuario_antes_da_alteracao,
                                 estado_atual=self.get_object())

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print('=' * 100)
        print(args)
        print(kwargs)
        print('=' * 100)

        #Auditoria.objects.create(tabela_operacao=self.nome_tabela_para_auditoria, tipo_operacao='CREATE',
        #                         usuario_operacao=request.user, estado_anterior='', estado_atual=self.get_object())

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
