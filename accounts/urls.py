
from django.urls import path
from .views import *

urlpatterns = [
    
   path('register/', SingUp.as_view(), name='singup')
    

   
]
