from django.db import models
from decimal import Decimal, DecimalException
# Create your models here.

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    evento = models.CharField(max_length=150)
    organizador = models.CharField(max_length=250)
    fecha = models.DateField()
    telefono = models.CharField(max_length=13)
    email = models.EmailField()
    meta = models.IntegerField(default=100000)
    costo = models.IntegerField(default=10000)
    direccion = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    # foto = models.ImageField(upload_to='eventos')
    latitud = models.DecimalField(max_digits=50, decimal_places=20, default=0)
    longitud = models.DecimalField(max_digits=50, decimal_places=20, default=0)
    
    def __str__(self):
        return self.evento
