from rest_framework import serializers
from productos.models import Producto



class ProductoSerializer(serializers.ModelSerializer):
    rama = serializers.SerializerMethodField()
    
    def get_rama(self, obj): 
         return obj.rama.nombre
    
    class Meta:
        model = Producto
        fields = '__all__'