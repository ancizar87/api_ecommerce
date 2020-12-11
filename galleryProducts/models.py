from django.db import models
from productos.models import Producto

# Create your models here.

class Imagenes(models.Model):
    service = models.ForeignKey(Producto, default=None, related_name="imagenes", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Imagen", null=False, blank=False, upload_to="ImagenesProducto", height_field=None, width_field=None, max_length=None)