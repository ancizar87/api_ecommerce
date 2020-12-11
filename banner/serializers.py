from rest_framework import serializers
from banner.models import *

class OrientacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientacion
        fields = '__all__'
        
class BannerSerializer(serializers.ModelSerializer):
    orientacion=serializers.SerializerMethodField()
    
    def get_orientacion(self, obj): 
         return obj.orientacion.orientacion
    
    class Meta:
        model = Banner
        fields = ['titulo','subtitulo','link','imagenfondo','imagenfrontal','orientacion']