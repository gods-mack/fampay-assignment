from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size = 5 # Number of objects to return in one page

    def generate_response(self, query_set, serializer_obj, request):
        try:
            page_data = self.paginate_queryset(query_set, request)
        except :
            return Response({"error": "No results found"}, status=status.HTTP_400_BAD_REQUEST)

        serialized_page = [serializer_obj(v) for v in page_data]
        return self.get_paginated_response(serialized_page)

    def paginated_resp(self, query_set, serializer_obj, request):
        return self.generate_response(query_set, serializer_obj, request)