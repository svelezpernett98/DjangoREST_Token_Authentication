from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from authentication_api.models import *
from authentication_api.serializers import *
from rest_framework.permissions import IsAuthenticated


class Prueba_modelo_viewset(viewsets.ModelViewSet):
    queryset = Prueba_modelo.objects.all()
    serializer_class = Prueba_modelo_serializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        self.serializer_class(self.queryset, many=True)
        return Response(self.serializer_class.data)

    def post(self, request, format=None):
        serialized_data_POST = self.serializer_class(data=request.data)
        if serialized_data_POST.is_valid():
            serialized_data_POST.save()
            return Response(serialized_data_POST.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data_POST.errors, status=status.HTTP_400_BAD_REQUEST)
