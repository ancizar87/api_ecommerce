from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from banner.models import Banner as BannerModel
from banner.serializers import BannerSerializer
from rest_framework.response import Response

# Create your views here.

class Banner(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request):        
        queryset = BannerModel.objects.all()
        serializer = BannerSerializer(queryset, many=True)
    
        return Response(serializer.data)