from django.urls import path
from . import views

app_name = "moto"
urlpatterns = [
    path('', views.index, name='index'),
    path("history/<str:type>", views.history, name="history"),
]