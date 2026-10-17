from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UsuarioForm

from moto.forms import motoForm
from moto.models import Moto
from .models import Usuario

from .services import validarLogin, verificarEmailUsuario, logarUsuario


# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        usuario = validarLogin(request, email, senha)
        logarUsuario(request, usuario)

        return redirect("usuario:home")

    return render(request, "usuario/login.html")

def cadastro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data["senha"])
            usuario.username = usuario.email

            usuario.save()

            logarUsuario(request, usuario)

            return redirect("usuario:home")
    else:
        form = UsuarioForm()

    return render(request, "usuario/cadastro.html", {
        "form": form
    })

def deslogar(request):
    logout(request)
    return redirect("usuario:login")

@login_required
def home(request):
    user = request.user
    motos = Moto.objects.filter(usuario=user.id)

    return render(request, "usuario/home.html", {
        "motos": motos
    })

@login_required
def addMoto(request):
    if request.method == 'POST':
        form = motoForm(request.POST)

        if form.is_valid():
            moto = form.save(commit=False)
            moto.usuario = request.user
            moto.save()

            return redirect('usuario:home')
    else:
        form = motoForm()

    context = {'form': form}
    return render(request, "moto/addMoto.html", context)

@login_required
def excluirMoto(request, moto_id):

    moto = get_object_or_404(Moto, id=moto_id, usuario=request.user)
    moto.delete()

    return redirect("usuario:home")