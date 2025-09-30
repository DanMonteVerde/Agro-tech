from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("terrenos/", views.terrenos, name="terrenos"),
    path("clima/", views.clima, name="clima"),
    path("calculadora/", views.calculadora, name="calculadora"),
    path("recomendacoes/", views.recomendacoes, name="recomendacoes"),
    path("produtos/", views.produtos, name="produtos"),
    path("dicas/", views.dicas, name="dicas"),
    path("contatos/", views.contatos, name="contatos"),
]