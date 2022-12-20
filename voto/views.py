from django.shortcuts import render

from .models import *

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
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selected_option = options.get(id = inputvalue)
        selected_option.vote +=5
        selected_option.save()
    return render(request, "resultado.html", {'question':question, 'options':options})
