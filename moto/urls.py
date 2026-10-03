from django.urls import path
from . import views

app_name = "moto"
urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_informacao', views.addInfo, name='addInfo'),
    path("history/<str:type>", views.history, name="history"),

    path("delete/<str:type>/<int:id>/", views.delete, name="delete"),
    path("update/<str:type>/<int:id>/", views.update, name="update"),
]