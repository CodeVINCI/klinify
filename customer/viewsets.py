from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.response import Response


class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()

    def list(self, request, *args, **kwargs):
        n = self.request.query_params.get("n", None)
        if n is None:
            queryset = models.Customer.objects.none()     
        else:
            queryset = models.Customer.objects.all().order_by('-dob')[:int(n)]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
