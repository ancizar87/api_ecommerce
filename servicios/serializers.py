from rest_framework import serializers
from servicios.models import Servicio
from galleryServices.serializers import ImagesSeralizer

class ServicioSerializer(serializers.ModelSerializer):
    images = ImagesSeralizer(many=True)
        
    class Meta:
        model = Servicio
        fields = '__all__'
