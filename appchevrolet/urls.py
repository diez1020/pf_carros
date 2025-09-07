from django.urls import path
from appchevrolet.views import chevrolet
urlpatterns = [
    path('chevrolet/', chevrolet),
]