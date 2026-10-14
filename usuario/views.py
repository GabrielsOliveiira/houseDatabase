from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm

from moto.models import Moto
from .models import Usuario

from .services import deleteMoto, adicionarMoto, validarLogin, verificarEmailUsuario, logarUsuario


# Create your views here.

def login(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        usuario = validarLogin(request, email, senha)
        logarUsuario(request, usuario)

        correto = "usuarioLogado"
        context = {"correto": correto}

    return render(request, "usuario/login.html", context)

def cadastro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data["senha"])
            usuario.username = [usuario.email]

            usuario.save()

            logarUsuario(request, usuario)

            return redirect("home")
    else:
        form = UsuarioForm()

    return render(request, "usuario/cadastro.html", {
        "form": form
    })

@login_required
def home(request):
    user = Usuario.objects.first()
    motos = Moto.objects.filter(usuario_id=user)

    return render(request, "usuario/home.html", {
        "motos": motos
    })

def addMoto(request):
    
    adicionarMoto()
    return redirect("home")

def excluirMoto(request, moto_id):

    deleteMoto(moto_id)
    return redirect("home")