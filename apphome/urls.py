from django.urls import path
from apphome.views import home
urlpatterns = [
    path('inicio/', home)
]