from django.db import models

# Create your models here.
class sponsor(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='media_home')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)