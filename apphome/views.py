from django.shortcuts import render
from apphome.models import sponsor
# Create your views here.
def home(request):
    spo = sponsor.objects.all()
    return render(request, 'apphome/inicio.html', {'sponsor': spo})