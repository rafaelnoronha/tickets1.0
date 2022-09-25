from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param
from collections import OrderedDict

class CustomPagination(pagination.LimitOffsetPagination):
    max_limit = 100

    def get_count(self, queryset):
        return None

    def paginate_queryset(self, queryset, request, view=None):
        self.limit = self.get_limit(request)

        if self.limit is None:
            return None

        self.count = self.get_count(queryset)
        self.offset = self.get_offset(request)
        self.request = request

        if self.template is not None:
            self.display_page_controls = True

        return list(queryset[self.offset:self.offset + self.limit])

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('próximo', self.get_next_link()),
            ('anterior', self.get_previous_link()),
            ('resultados', data)
        ]))

    def get_next_link(self):
        url = self.request.build_absolute_uri()
        url = replace_query_param(url, self.limit_query_param, self.limit)

        offset = self.offset + self.limit
        return replace_query_param(url, self.offset_query_param, offset)
