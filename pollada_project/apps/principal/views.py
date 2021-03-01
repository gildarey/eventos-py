from django.shortcuts import render
from .models import Evento
from .formulario import EventoForm

# Create your views here.

from .models import Evento

def inicio(request):
    eventos = Evento.objects.all()
    print(eventos)
    return render(request, 'index.html', {'eventos': eventos})

def crearEvento(request):
    if request.method == 'GET':
        form = EventoForm()
    else:
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_evento.html', {'form' : form})