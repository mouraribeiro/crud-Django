from django import forms 

from .models import Restaurante

class RestauranteForm(forms.ModelForm):

    class Meta:
        model = Restaurante
        fields = ('nome', 'description', 'codigo')






    