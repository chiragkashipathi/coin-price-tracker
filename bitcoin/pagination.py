from rest_framework import pagination
from rest_framework.response import Response


class APIPagination(pagination.PageNumberPagination):

    page_size_query_param = 'offset'
    page_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'data': data,
            },  
        )

