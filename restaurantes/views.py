from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Restaurante
from .forms import RestauranteForm
from django.contrib import messages
from django.views.generic import ListView


# Create your views here.
@login_required
def restauranteList(request):
    restaurante_list = Restaurante.objects.all().order_by('-created_at')

    paginator = Paginator(restaurante_list, 3)

    page = request.GET.get('page')

    restaurante = paginator.get_page(page)  # tasks

    return render(request, 'restaurante/list.html', {'restaurante': restaurante})


def restauranteView(request, id):
    restaurante = get_object_or_404(Restaurante, pk=id)
    return render(request, 'restaurante/view.html', {'restaurante': restaurante})

@login_required
def newRestaurante(request):
    if request.method == 'POST':
        form = RestauranteForm(request.POST)

        if form.is_valid():
            restaurante = form.save(commit=False)
            restaurante.save()
            return redirect('/')
    else:
        form = RestauranteForm()
        return render(request, 'restaurante/addrestaurante.html', {'form': form})

@login_required
def editRestaurante(request, id):
    restaurante = get_object_or_404(Restaurante, pk=id)
    form = RestauranteForm(instance=restaurante)

    if request.method == 'POST':
        form = RestauranteForm(request.POST, instance=restaurante)

        if (form.is_valid()):
            restaurante = form.save(commit=False)
            restaurante.save()
            return redirect('/')
        else:
            return render(request, 'restaurante/edit_restaurante.html', {'form': form, 'restaurante': restaurante})
    else:
        return render(request, 'restaurante/editrestaurante.html', {'form': form, 'restaurante': restaurante})

@login_required
def deleteRestaurante(request, id):
    restaurante = get_object_or_404(Restaurante, pk=id)
    restaurante.delete()
    messages.info(request, 'Restaurante deletado com sucesso!')
    return redirect('/')




