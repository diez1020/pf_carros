from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contacto(request):
    return render(request, 'appcontacto/contacto.html')


def respuesta(request):
        if request.method == "POST":
            subject = request.POST['asunto']
            message = f"Marca: {request.POST['eleccion']} \n Modelo: {request.POST['modelo']}\n\nEmail de contacto: {request.POST['email']} \n Numero: {request.POST['numero']}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['diez10020@gmail.com']

            send_mail(subject, message, from_email, recipient_list)
            return render(request, 'appcontacto/respuesta_form.html')
        return render(request, 'appcontacto/contacto.html')