from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

from moto.models import Moto
from .models import Usuario

def verificarEmailUsuario(email):
    return 1 if Usuario.objects.filter(email=email).exists() else 0

def validarLogin(request, email, senha):
    usuario = authenticate(request, username=email, password=senha) 
    if usuario:
        return usuario
    raise Exception("Email ou senha inválidos")

def logarUsuario(request, usuario):
    login(request, usuario)
    return 1