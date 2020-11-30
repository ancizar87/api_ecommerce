from rest_framework import serializers
from ramas.models import Ramal

class RamalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ramal
        fields = '__all__'
    