from django.db import models

# Create your models here.
class vehiculos(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    motor = models.TextField()
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='media_vehiculos')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)