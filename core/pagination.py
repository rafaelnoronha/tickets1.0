from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    def get_count(self, queryset):
        return len(queryset)

    def paginate_queryset(self, queryset, request, view=None):
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.count = self.get_count(queryset)
        self.offset = self.get_offset(request)
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        # if self.count == 0 or self.offset > self.count:
        #     return []
        return list(queryset[self.offset:self.offset + self.limit])

    def get_paginated_response(self, data):
        return Response({
            'proxima': self.get_next_link(),
            'anterior': self.get_previous_link(),
            'resultados': data
        })