from rest_framework import serializers
from unidadMedida.models import UnidadM

class unidadMSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UnidadM
        fields = '__all__'