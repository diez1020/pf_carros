from django.urls import path
from apptoyota.views import toyota
urlpatterns = [
    path('toyota/', toyota),
]