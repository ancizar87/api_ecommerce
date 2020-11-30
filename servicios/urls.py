from django.urls import path
from servicios.views import Servicio


urlpatterns = [
    path('',Servicio.as_view()),

]