from django.urls import path

from . import views

app_name = "moto"
urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('adicionar_informacao/<int:id>', views.addInfo, name='addInfo'),
    path("history/<str:type>/<int:id>", views.history, name="history"),
    path("oleo/verificar/<int:id>/", views.check_oil, name="check_oil"),

    path("delete/<str:type>/<int:id>/", views.delete, name="delete"),
    path("update/<str:type>/<int:id>/", views.update, name="update"),
]