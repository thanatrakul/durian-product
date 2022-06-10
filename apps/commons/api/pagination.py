from collections import OrderedDict
from django.conf import settings
from rest_framework.utils.urls import replace_query_param
from rest_framework.views import Response
from rest_framework_json_api.pagination import PageNumberPagination


class PageNumberPaginationMixin(PageNumberPagination):
    """
    A json-api compatible pagination format
    """

    page_size_query_param = settings.API_PAGINATE_BY_PARAM
    max_page_size = settings.API_MAX_PAGE_SIZE

    def build_link(self, index):
        if not index:
            return None
        url = self.request and self.request.build_absolute_uri() or ''
        return replace_query_param(url, self.page_query_param, index)

    def get_paginated_response(self, data):
        next = None
        previous = None

        if self.page.has_next():
            next = self.page.next_page_number()
        if self.page.has_previous():
            previous = self.page.previous_page_number()

        return Response({
            'results': data,
            'meta': OrderedDict([
                ('page', self.page.number),
                ('pages', self.page.paginator.num_pages),
                ('perpage', settings.API_PAGE_SIZE),
                ('total', self.page.paginator.count),
            ]),
            'links': OrderedDict([
                ('first', self.build_link(1)),
                ('last', self.build_link(self.page.paginator.num_pages)),
                ('next', self.build_link(next)),
                ('prev', self.build_link(previous))
            ])
        })
