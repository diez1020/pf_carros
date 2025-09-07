from django.urls import path
from appcontacto.views import contacto, respuesta
urlpatterns = [
    path('contacto/', contacto),
    path('contacto/respuesta_contacto/', respuesta)
]