from django.shortcuts import render
from apptoyota.models import hoteles
# Create your views here.
def ubicacion (request):
    ht = hoteles.objects.all()
    return render(request, 'apptoyota/ubicacion.html', {'hotel': ht})

