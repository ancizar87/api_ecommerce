from django.urls import path
from productos.views import ProductoListView, PaginadorListView, produclastListView, ProductofilterListView, Productofilter, producpromocionlastListView, Favoritos

urlpatterns = [
    path('',ProductoListView.as_view()),
    path('buscar/',ProductoListView.as_view()),
    path('paginas/',PaginadorListView.as_view()),
    path('last/',produclastListView.as_view()),
    path('fcategoria/',ProductofilterListView.as_view()),
    path('<id>/',Productofilter.as_view()),
    path('promocion/',producpromocionlastListView.as_view()),
    path('favorito/', Favoritos.as_view()),
]

