from django.contrib import admin
from django.contrib.admin.options import TabularInline

# Register your models here.
from .models import Restaurante



admin.site.register(Restaurante)

