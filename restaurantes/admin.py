from django.contrib import admin
from django.contrib.admin.options import TabularInline

# Register your models here.
from .models import Restaurante
from voto.models import *


admin.site.register(Restaurante)
admin.site.register(Pergunta)
admin.site.register(Escolha)


