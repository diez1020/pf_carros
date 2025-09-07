from django.shortcuts import render
from apptoyota.models import toyotas
# Create your views here.
def toyota (request):
    toyo = toyotas.objects.all()
    return render(request, 'apptoyota/toyota.html', {'toyota':toyo})