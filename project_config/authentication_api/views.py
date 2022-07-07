from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
import requests
from authentication_api.viewsets import Prueba_modelo_viewset
# Create your views here.

#METODO PARA CREAR TOKEN CON @API_VIEW
# @api_view(['POST'])
# def login(request):
    
#     username = request.POST.get('username')
#     password = request.POST.get('password')
    
#     try:
#         user =User.objects.get(username=username)
#     except User.DoesNotExist:
#         return Response("Usuario no valido")
    
#     pwd_valid = check_password(password, user.password)
    
#     if not pwd_valid:
#         return Response("Contraseña no valida")
    
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response(token.key)

def get_token_form(request):
    return render(request, 'get_token.html')

def login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user =User.objects.get(username=username)
        except User.DoesNotExist:
            return Response("Usuario no valido")
        
        pwd_valid = check_password(password, user.password)
        
        if not pwd_valid:
            return Response("Contraseña no valida")
        
        token, _ = Token.objects.get_or_create(user=user)

        context = {}
        context['token'] = token.key
        
        return render(request, 'authorized_user.html', context)
    

def show_model(request):
    url = 'http://localhost:8000/prueba-modelo'
    token = '0698de8e0873c952e3dabaf51a0bc151de6c8920'
    headers = {'Authorization': 'Token 0698de8e0873c952e3dabaf51a0bc151de6c8920'}

    r = requests.get('http://localhost:8000/get-token-form/', headers={'Authorization': 'Token c6251920cfa860c5c27b2b98939b5c59950cee3f'})
    
    prueba_modelo_obj = Prueba_modelo_viewset()
    
    return r
        


