from rest_framework import serializers
from shoppingcar.models import Cart
from productos.serializers import ProductoSerializer

class CartSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=False, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['usuario','productos','cantidad','precio_unidad','precio_total','fecha']
        #precio_total = serializers.IntegerField(required=True, label)