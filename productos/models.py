from django.db import models
from ramas.models import Ramal
from unidadMedida.models import UnidadM
from rest_framework.fields import JSONField
from django.contrib.auth.models import User


# Create your models here.

class Producto(models.Model):
    rama = models.ForeignKey(Ramal, verbose_name="Rama", on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre del producto", blank=False, null=False, max_length=100)
    promocion = models.BooleanField(verbose_name="Promocion", blank=True, null=True)
    actions = JSONField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created']
        
    def __str__(self):
        return self.nombre
    