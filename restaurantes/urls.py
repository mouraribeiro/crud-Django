
from django.urls import path
from django.views.generic import ListView

from .views import *
#restauranteList, editRestaurante,deleteRestaurante, selectRestaurante from .views import
# restauranteView, newRestaurante


urlpatterns = [
    
    path('', restauranteList, name= 'restaurante-list'),
    path('restaurante/<int:id>', restauranteView, name="restaurante-view"),
    path('addrestaurante/', newRestaurante, name='new-restaurante'),
    path('edit/<int:id>', editRestaurante, name='edit-restaurante'),
    path('delete/<int:id>', deleteRestaurante, name='delete-restaurante'),
    path('select/',selectList, name='voto_list'),
    
   
    

   
]
