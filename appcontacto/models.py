from django.db import models

# Create your models here.
class contacto(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='media_contacto')