from django.urls import path
from appford.views import ford
urlpatterns = [
    path('ford/', ford),
]