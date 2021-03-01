from django.db import models

# Create your models here.

class Evento(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 150)
    organizador = models.CharField(max_length = 150, default='')
    contacto = models.CharField(max_length = 150, default='')
    fecha = models.DateField(default='')
    tipo = models.CharField(max_length = 150, default='')
    organizado_para = models.CharField(max_length = 250)
    direccion = models.CharField(max_length=200, default='')
    ciudad = models.CharField(max_length=50, default='')
    descripcion = models.CharField(max_length=350, default='')
    costo = models.IntegerField(default=10000)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.nombre

