from django.urls import path
from appchevrolet.views import carros
urlpatterns = [
    path('carros/', carros)
]