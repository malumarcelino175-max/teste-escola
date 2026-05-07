from django.urls import path
from . import views

app_name = "alunos"

urlpatterns = [
    path("lista/", views.lista_view, name="lista"),
    path("novo/", views.novo_view, name="novo"),
    path("detalhe/", views.detalhe_view, name="detalhe"),
]