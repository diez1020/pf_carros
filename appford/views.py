from django.shortcuts import render
from appford.models import fords
# Create your views here.

def acerca (request):
    return render(request, 'appford/acerca.html')