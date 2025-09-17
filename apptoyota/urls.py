from django.urls import path
from apptoyota.views import ubicacion
urlpatterns = [
    path('ubicacion/', ubicacion),
]