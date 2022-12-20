from django.db import models

from restaurantes.models import Restaurante
from django.contrib.auth.models import User

# Create your models here.


class Pergunta(models.Model):    
    question = models.CharField( max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.question
    

class Escolha(models.Model):  
    
    question = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name ="choices")
    option = models.CharField( max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option
