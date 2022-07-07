from urllib import request
from rest_framework import routers
from authentication_api.views import *
from authentication_api.viewsets import *

router = routers.DefaultRouter()
router.register(r'prueba-modelo', Prueba_modelo_viewset)
