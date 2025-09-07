from django.shortcuts import render
from appchevrolet.models import chevys
# Create your views here.
def chevrolet(request):
    chev = chevys.objects.all()
    return render(request, 'appchevrolet/chevrolet.html', {'chevy':chev})