from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from caractproducto.views import  CaracteristicaListView, Caracteristica_view, CaracteristicaPromo, Caracteristica, FiltroRetrieveUpdateAPIView


urlpatterns = [
     path('buscar/',CaracteristicaListView.as_view()),
    path('caract/update/', Caracteristica_view, name="id"),
    path('promocion/', CaracteristicaPromo.as_view()),
    path('caract/', Caracteristica.as_view()),
    path('filtro/<id>/', FiltroRetrieveUpdateAPIView.as_view()),
    path('update/<id>/', FiltroRetrieveUpdateAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

