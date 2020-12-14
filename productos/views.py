from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from rest_framework.views import  APIView
from rest_framework import filters
from rest_framework import pagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from productos.serializers import ProductoSerializer
from productos.models import Producto as ProductoModel
from rest_framework import generics
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.fields import JSONField

# Create your views here.

class ProductosPagination(pagination.PageNumberPagination):
    permission_classes = (AllowAny,)
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
    last_page_strings = ('last',)
    
    
class PaginadorListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ProductoModel.objects.all()
    serializer_class = ProductoSerializer
    pagination_class =  ProductosPagination

class ProductoListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ProductoModel.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']
    
class Productofilter(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request, id):        
        queryset = ProductoModel.objects.all().filter(id=id)
        serializer = ProductoSerializer(queryset, many=True)
    
        return Response(serializer.data)    
    
class produclastListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ProductoModel.objects.all().order_by('-id')[:8][::-1]
    serializer_class = ProductoSerializer
    
class producpromocionlastListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ProductoModel.objects.all().order_by('-id')[:8][::-1]
    serializer_class = ProductoSerializer

class ProductofilterListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ProductoModel.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['rama__nombre', 'promocion']