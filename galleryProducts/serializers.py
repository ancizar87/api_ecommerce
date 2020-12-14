from rest_framework import serializers
from .models import Imagenes

class ImagenesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = '__all__'