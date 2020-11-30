from rest_framework import serializers
from orders.models import Order, OrderItem
#from dastosUsuario.serializers import DatosSerializer



class OrderSerializer(serializers.ModelSerializer):
    
    #direccion = serializers.SerializerMethodField()
    
    #def get_direccion(self, obj): 
     #    return obj.direccion.Shipping_Address
    
    class Meta:
        model = Order
        fields = ['id', 'usuario','estado', 'precio_total', 'invoice_no','fecha']
        
        
class OrderItemSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = OrderItem
        fields = ['id','producto','orden','precio','cantidad']