from django.urls import path
from ramas.views import RamalList



urlpatterns = [
    path('', RamalList.as_view())
]