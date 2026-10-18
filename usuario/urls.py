from django.urls import path

from . import views

app_name = "usuario"

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("home/", views.home, name="home"),
    path("moto/adicionar", views.addMoto, name="addMoto"),
    path("moto/excluir/<int:moto_id>/", views.excluirMoto, name="delMoto"),
    path("login/", views.login, name="login"),
    path("logout/", views.deslogar, name="logout"),
]
