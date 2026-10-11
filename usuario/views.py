from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UsuarioForm
from moto.models import Moto
from .models import Usuario


# Create your views here.

def cadastro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("cadastro")
    else:
        form = UsuarioForm()

    return render(request, "usuario/cadastro.html", {
        "form": form
    })

def home(request):
    
    return render(request, "usuario/home.html")
