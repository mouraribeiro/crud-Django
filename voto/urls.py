from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "index"),
   
    path("voto/<str:pk>",votos, name = "votos"),
    path("resultado/<str:pk>", resultado, name = "resultado"),
]