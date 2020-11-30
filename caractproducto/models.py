from django.db import models
from productos.models import Producto
from unidadMedida.models import UnidadM

# Create your models here.

class Caracteristica(models.Model):
    opcion = models.ForeignKey(Producto, verbose_name="Opcion", related_name="opcionCaracteristica", on_delete=models.CASCADE)
    codigoP = models.CharField(verbose_name="Codigo", null=False, blank=False, max_length=50)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=100, help_text="respuesta segun pregunta anterior")
    precio = models.CharField(verbose_name="Precio", max_length=50, null=False, blank=False)
    precioPromo = models.CharField(verbose_name="precio promo", max_length=50, null=True, blank=True)  
    minimo = models.IntegerField(verbose_name="Pedido minimo", default=1, blank=False, null=False)  
    disponibles = models.IntegerField(verbose_name="Disponibles", blank=False, null=False)
    UMedida = models.ForeignKey(UnidadM, verbose_name="Unidad de medida", on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name="opcionCaracteristica"
        verbose_name_plural = "opcionCaracteristicas"
        ordering = ['id']
        
    def __str__(self):
        return self.codigoP