from django.shortcuts import render
from django.conf import settings
from .models import Evento
from .form import EventoForm
from django.http import JsonResponse
from decimal import Decimal, DecimalException
from django.core import serializers
from django.http import HttpResponse

def inicio(request):
    return render(request, 'index.html')


def getEventos(request):
    if request.is_ajax and request.method == "GET":
        ciudad = request.GET.get("ciudad", None)
        if Evento.objects.filter(ciudad = ciudad).exists():
            eventos = Evento.objects.filter(ciudad=ciudad)[:5]
            data = serializers.serialize('json', list(eventos))
            #  fields=('id','evento','organizador','fecha','telefono','email','meta','costo','direccion','ciudad','descripcion','latitud','longitud')
            return JsonResponse(data, status = 200, safe=False)
        else:
            return JsonResponse({"found": False}, status = 200, safe=False)

    return JsonResponse({}, status = 400)
    

def eventos(request):
    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'eventos.html', context)

def crearEvento(request):
    form = EventoForm()
    response_data = {}

    if request.POST.get('action') == 'post':
        try:
            evento = request.POST.get('evento')
            organizador = request.POST.get('organizador')
            fecha = request.POST.get('fecha')
            telefono = request.POST.get('telefono')
            email = request.POST.get('email')
            meta = request.POST.get('meta')
            costo = request.POST.get('costo')
            direccion = request.POST.get('direccion')
            ciudad = request.POST.get('ciudad')
            descripcion = request.POST.get('descripcion')
            

            lng = Decimal(request.POST.get('long'))
            lat = Decimal(request.POST.get('lat'))


            Evento.objects.create(
             evento = evento,
             organizador = organizador,
             fecha = fecha,
             telefono = telefono,
             email = email,
             meta = meta,
             costo = costo,
             direccion = direccion,
             ciudad = ciudad,
             descripcion = descripcion,
             latitud = lat,
             longitud = lng
             ) 
        except (ValueError, DecimalException):
            response_data['error'] = 'DecimalException'
            print("Error! ...")
            # print(e)
        except Exception as e:
            print(e)
            response_data['error'] = 'error'
            return JsonResponse(response_data)
        
        
        response_data['title'] = 'title'
        response_data['description'] = 'description'
        return JsonResponse(response_data)

    return render(request, 'form.html', {'form': form, 'api_key': settings.GOOGLE_MAPS_API_KEY})

def int_or_0(value):
    try:
        return int(value)
    except:
        return 0