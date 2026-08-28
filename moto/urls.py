from django.urls import path
from . import views

app_name = "moto"
urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_informacao', views.addInfo, name='index'),
    path("history/<str:type>", views.history, name="history"),
    path("delete/washed/<int:id>/", views.delete_washed, name="delete_washed"),
    path("update/washed/<int:id>/", views.update_washed, name="update_washed")
]