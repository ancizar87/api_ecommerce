from django.db import models
from productos.models import Producto
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Cart(models.Model):
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    productos = models.ForeignKey(Producto, verbose_name="Productos", on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unidad = models.IntegerField()
    precio_total = models.IntegerField()
    fecha = models.DateTimeField(verbose_name="Fecha", default=now)
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['-id']

    def __str__(self):
        return "Cart {}".format(self.usuario)