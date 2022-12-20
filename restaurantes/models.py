from django.db import models
 

# Create your models here.
class Restaurante(models.Model):
    
    nome = models.CharField(max_length=255)
    description = models.TextField()
    codigo = models.CharField(max_length=15)  
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome
