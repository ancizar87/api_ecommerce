from django.db import models
from caractproducto.models import Caracteristica
#from dastosUsuario.models import Datos
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from django.utils.timezone import now

# Create your models here.

def increment_invoice_number():
    last_invoice = Order.objects.all().order_by('id').last()
    if not last_invoice:
        return 'FVW0001'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split('FVW')[-1])
    width = 4
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    #cod_no = '{:03}'.format(random.randrange(1,10**3))
    new_invoice_no = 'FVW' + str(formatted) #+ str(cod_no)
    return new_invoice_no  


class Order(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #direccion = models.ForeignKey(Datos, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    precio_total = models.IntegerField()
    invoice_no = models.CharField(max_length=500, default=increment_invoice_number, null=True, blank=True)
    fecha = models.DateTimeField(verbose_name="Fecha", default=now)
    
    class Meta:
        verbose_name="Order"
        verbose_name_plural = "Orders"
        ordering = ['-id']
 
    def __str__(self):
        return 'Order {}'.format(self.invoice_no)
    
    
class OrderItem(models.Model):
    producto = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    orden = models.ForeignKey(Order, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.cantidad


@receiver(post_save, sender = Order)
def delete_order_items(sender, instance, **kwargs):
    # Si entra al if, es que la orden ha sido aprobada
    if instance.estado == 'aprobado':
        for order_item in instance.orderitem_set.all():
            order_item.producto.disponibles = abs(order_item.cantidad - order_item.producto.disponibles)
            order_item.producto.save() 