from django.shortcuts import render
from appford.models import fords
# Create your views here.
def ford (request):
    frd = fords.objects.all()
    return render(request, 'appford/ford.html', {'ford':frd})
