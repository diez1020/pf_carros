from django.shortcuts import render
from appchevrolet.models import vehiculos
# Create your views here.

def carros(request):
    vehi = vehiculos.objects.all()
    return render(request, 'appchevrolet/carros.html', {'carros': vehi})