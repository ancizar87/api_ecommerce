from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from servicios.models import Servicio as ServicioModel
from servicios.serializers import ServicioSerializer

# Create your views here.

class Servicio(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request):        
        queryset = ServicioModel.objects.all()
        serializer = ServicioSerializer(queryset, many=True)
    
        return Response(serializer.data)
    