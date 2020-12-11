from django.shortcuts import get_object_or_404, render
from rest_framework.views import  APIView
from rest_framework.decorators import api_view, permission_classes
from caractproducto.serializers import CaracteristicaSerializer
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from caractproducto.models import Caracteristica as CaracteristicaModel
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.generics import  RetrieveUpdateAPIView
#from orders.models import Order as OrderModel


# Create your views here.

class CaracteristicaListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = CaracteristicaModel.objects.all()
    serializer_class = CaracteristicaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['codigoP','descripcion']

class Caracteristica(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request):        
        queryset = CaracteristicaModel.objects.all()
        serializer = CaracteristicaSerializer(queryset, many=True)
    
        return Response(serializer.data)
    

class CaracteristicaPromo(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request):        
        queryset = CaracteristicaModel.objects.exclude(precioPromo__isnull=True).exclude(precio__exact='')
        serializer = CaracteristicaSerializer(queryset, many=True)
    
        return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes([AllowAny, ])
def Caracteristica_view(request, id, format=None):

    
    try:
        caracteristica = CaracteristicaModel.objects.get(id=id)
    except CaracteristicaModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CaracteristicaSerializer(caracteristica)
        return Response(serializer.data)
    
    
    elif request.method == "PUT":
        serializer = CaracteristicaSerializer(caracteristica, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfull"
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class FiltroRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request, id):
        auxi_espec = id
        auxi_espec_lst = [int(x.strip()) for x in auxi_espec.split(',') if x]
        caracteristica = CaracteristicaModel.objects.filter(id__in=auxi_espec_lst)
        serializer = CaracteristicaSerializer(caracteristica, many=True) 
    
        return Response(serializer.data)
    
    
    def put(self, request, id):
        auxi_espec = id
        auxi_espec_lst = [int(x.strip()) for x in auxi_espec.split(',') if x]
        caracteristica = CaracteristicaModel.objects.filter(id__in=auxi_espec)
        serializer = CaracteristicaSerializer(caracteristica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
