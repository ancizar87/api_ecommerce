from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import  APIView
from orders.models import Order as OrderModel
from orders.models import OrderItem as OrderItemModel
from orders.serializers import OrderItemSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from caractproducto.models import Caracteristica
from caractproducto.serializers import CaracteristicaSerializer
from django.core.mail import send_mail
from django.template import Context, loader
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from usuario.settings import EMAIL_HOST_USER

# Create your views here.

class Order(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):        
        queryset = OrderModel.objects.all()
        serializer = OrderSerializer(queryset, many=True)
    
        return Response(serializer.data)
    
    def post(self,request):
        serializer = OrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def Order_view(request, invoice_no, format=None):

    
    try:
        order = OrderModel.objects.get(invoice_no=invoice_no)
    except OrderModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    
    elif request.method == "PUT":
        serializer = OrderSerializer(order, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfull"
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Orders(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, usuario):        
        queryset = OrderModel.objects.all().filter(usuario=usuario)
        serializer = OrderSerializer(queryset, many=True)
    
        return Response(serializer.data)
    
    
class OrderItem(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):        
        queryset = OrderItemModel.objects.all()
        serializer = OrderItemSerializer(queryset, many=True)
    
        return Response(serializer.data)
    
    def post(self,request):
        serializer = OrderItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Orderitems(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, orden):        
        queryset = OrderItemModel.objects.all().filter(orden=orden)
        serializer = OrderItemSerializer(queryset, many=True)
    
        return Response(serializer.data)
    
    
#def orderEmail(request):
    
 #   if request.method == 'POST':
  #      if estado_aprobado:
            
            
    
    

   #     def post(self, request, *args, **kwargs):
    #        invoice_no = request.data.get('invoice_no')
     #       producto = request.data.get('producto')
      #      cantidad = request.data.get('cantidad')
       #     precio = request.data.get('precio')
        #    precio_total = request.data.get('precio_total')
         #   usuario = request.data.get('usuario')
          #  fecha = request.data.get('fecha')
        
        #    body = render_to_string(
         #       'factura.html', {
          #      'invoice_no': invoice_no,
           #     'producto': producto,
            #    'cantidad': cantidad,
             #   'precio': precio,
              #  'precio_total': precio_total,
               # 'usuario': usuario,
              #  'fecha': fecha,
               #  },
           # )

            #email_message = EmailMessage(
            #body=body,
            #from_email=email,
            #to=[EMAIL_HOST_USER],
            #)
            #email_message.content_subtype = 'html'
            #email_message.send()
        
        
            #return Response({"success": "Sent"})
        
    

#def post(self, request, *args, **kwargs):
  #          context = {
   #             'invoice_no':'invoice',
    #            'producto': 'producto',
     #           'cantidad': 'cantidad',
      #          'precio': 'precio',
       #         'precio_total': 'precio_total',
        #        'usuario': 'usuario',
         #       'fecha': 'fecha'
          #  }
        
           # factura.html = loader.get_template('orders/factura.html')
            
            #email.send()
        
            #return redirec('aprobado')
            