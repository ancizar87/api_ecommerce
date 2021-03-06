from rest_framework import serializers
from productos.models import Producto
from caractproducto.serializers import CaracteristicaSerializer
from galleryProducts.serializers import ImagenesSeralizer


class ProductoSerializer(serializers.ModelSerializer):
    opcionCaracteristica = CaracteristicaSerializer(many=True)
    imagenes = ImagenesSeralizer(many=True)
    rama = serializers.SerializerMethodField()
    
    def get_rama(self, obj): 
         return obj.rama.nombre
    
    class Meta:
        model = Producto
        fields = '__all__'