from rest_framework import serializers
from .models import Caracteristica
from unidadMedida.models import UnidadM
from unidadMedida.serializers import unidadMSerializer

class CaracteristicaSerializer(serializers.ModelSerializer):
    UMedida = serializers.SerializerMethodField()
    
    def get_UMedida(self, obj): 
         return obj.UMedida.medida
    
    class Meta:
        model = Caracteristica
        fields = '__all__'