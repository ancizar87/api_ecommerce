from django.shortcuts import render
from rest_framework.views import  APIView
from terminosCondiciones.models import TerminosCondiciones
from terminosCondiciones.serializers import TerminosCondicionesSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.

class Terminos(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):        
        queryset = TerminosCondiciones.objects.all()
        serializer = TerminosCondicionesSerializer(queryset, many=True)
    
        return Response(serializer.data)
    