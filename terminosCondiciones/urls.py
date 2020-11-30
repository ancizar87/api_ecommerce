from django.urls import path
from terminosCondiciones.views import *

urlpatterns = [
    path('terminos/',Terminos.as_view()),
]