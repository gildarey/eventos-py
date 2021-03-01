from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        # fields = ('nombre', 'organizador','contacto', 'fecha', 
        #         'organizado_para', 'direccion', 'ciudad', 'descripcion', 'costo',)
        fields = '__all__'
        