from django.shortcuts import render,redirect, get_object_or_404

from datetime import datetime
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    questions = Pergunta.objects.all()
    return render(request, "index.html", {'questions':questions})


def votos(request,pk):
    question = Pergunta.objects.get(id=pk)
    options = question.choices.all()
    

    return render(request, "votos.html", {'question': question, 'options':options})


def resultado(request,pk):
     
    question = Pergunta.objects.get(id=pk)
    options = question.choices.all() 
    hora_atual = datetime.now().time()
    hora_atual = hora_atual.strftime("%H")
    print("hora_atual:", hora_atual)

    hora_atual = int(hora_atual)
    print(hora_atual)

    if hora_atual > 11 and hora_atual < 14:
        print('Tá liberado')
        if request.method == 'POST':
            inputvalue = request.POST['choice']
            selected_option = options.get(id = inputvalue)
            selected_option.vote +=5
            selected_option.save()
            messages.info(request, 'Horário de votos encerrado!')
        return render(request, "resultado.html", {'question':question, 'options':options})



 # Verify if the voter has voted or not


