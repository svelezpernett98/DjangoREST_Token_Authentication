from authentication_api.models import *
from rest_framework import serializers

class Prueba_modelo_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prueba_modelo
        fields = ['nombre', 'apellido', 'correo', 'fecha_de_creacion']

