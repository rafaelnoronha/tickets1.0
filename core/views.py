from auditoria.models import Auditoria
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.viewsets import GenericViewSet


class CreateModelMixinAuditoria(mixins.CreateModelMixin):
    auditoria = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        dado_criado = self.auditoria['serializer'](
            self.auditoria['modelo'].objects.get(uuid=serializer.data['uuid']))

        Auditoria.objects.create(tabela_operacao=self.auditoria['nome_tabela'], tipo_operacao='CREATE',
                                 usuario_operacao=request.user, estado_anterior='', estado_atual=dado_criado.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UpdateModelMixinAuditoria(mixins.UpdateModelMixin):
    auditoria = None

    def update(self, request, *args, **kwargs):
        dado_antes_alteracao = self.auditoria['serializer'](
            self.auditoria['modelo'].objects.get(id=self.get_object().id))
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        dado_depois_alteracao = self.auditoria['serializer'](
            self.auditoria['modelo'].objects.get(id=self.get_object().id))

        Auditoria.objects.create(tabela_operacao=self.auditoria['nome_tabela'], tipo_operacao='UPDATE',
                                 usuario_operacao=request.user, estado_anterior=dado_antes_alteracao.data,
                                 estado_atual=dado_depois_alteracao.data)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class DestroyModelMixinAuditoria(mixins.DestroyModelMixin):
    auditoria = None

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        Auditoria.objects.create(tabela_operacao=self.auditoria['nome_tabela'], tipo_operacao='DELETE',
                                 usuario_operacao=request.user, estado_anterior=self.auditoria['serializer'](instance).data,
                                 estado_atual='')

        return Response(status=status.HTTP_204_NO_CONTENT)


class ModelViewSetComAuditoria(CreateModelMixinAuditoria, mixins.RetrieveModelMixin, UpdateModelMixinAuditoria,
                               DestroyModelMixinAuditoria, mixins.ListModelMixin, GenericViewSet):
    pass
