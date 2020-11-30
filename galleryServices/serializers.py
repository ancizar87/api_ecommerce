from rest_framework import serializers
from galleryServices.models import Images


class ImagesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'