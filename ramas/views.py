from django.shortcuts import render
from ramas.models import Ramal as RamalModel
from rest_framework.response import Response
from ramas.serializers import RamalSerializer
from rest_framework import generics

#from rest_framework.views import  APIView

# Create your views here.


#class Ramal(APIView):
 #   permission_classes = (AllowAny,)
    
  #  def get(self, request):        
   #     queryset = RamalModel.objects.all()
    #    serializer = RamalSerializer(queryset, many=True)
    
     #   return Response(serializer.data)
    
class RamalList(generics.ListCreateAPIView):
    
    queryset = RamalModel.objects.all()
    serializer_class = RamalSerializer
    

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = RamalSerializer(queryset, many=True)
        return Response(serializer.data)