from django.db import models

# Create your models here.

class Servicio(models.Model):
    title = models.CharField(verbose_name="Titulo", blank=False, null=False, max_length=50)
    image = models.ImageField(verbose_name="Imagen de fondo", upload_to='servicios', height_field=None, width_field=None, max_length=None)
    content = models.TextField(verbose_name="Contenido", blank=False, null=False, max_length=500)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-created']
        
    def __str__(self):
        return self.title