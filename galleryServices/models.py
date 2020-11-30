from django.db import models
from servicios.models import Servicio

# Create your models here.

class Images(models.Model):
    service = models.ForeignKey(Servicio, default=None, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Imagen", upload_to="Image", height_field=None, width_field=None, max_length=None)