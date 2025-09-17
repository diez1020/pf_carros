from django.db import models

# Create your models here.
class hoteles(models.Model):
    nombre = models.CharField(max_length=50)
    distancia = models.TextField()
    imagen = models.ImageField(upload_to='media_hoteles')
    precio = models.CharField(max_length=80)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)