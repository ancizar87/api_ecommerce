from django.db import models

# Create your models here.

class Orientacion(models.Model):
    orientacion = models.CharField(verbose_name="Orientacion", null=False, blank=True, max_length=50)
    
    class Meta:
        verbose_name = "Orientacion"
        verbose_name_plural = "Orientacions"
        ordering = ['-id']
        
    def __str__(self):
        return self.orientacion

class Banner(models.Model):
    titulo = models.CharField(verbose_name="Titulo", blank=True, null=True, max_length=50)
    subtitulo = models.CharField(verbose_name="Subtitulo", blank=True, null=True,max_length=50)
    link = models.CharField(verbose_name="Link", blank=True, null=True, max_length=50)
    imagenfondo = models.ImageField(verbose_name="Imagenfondo", blank=True, null=True, upload_to="Imagenfondo", height_field=None, width_field=None, max_length=None)
    imagenfrontal = models.ImageField(verbose_name="Imagenfrontal", blank=True, null=True, upload_to="Imagenfrontal", height_field=None, width_field=None, max_length=None)
    orientacion = models.ForeignKey(Orientacion, verbose_name="Orientacion", blank=False, null=False, on_delete=models.CASCADE)
   
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
        ordering = ['-id']
        
    def __str__(self):
        return self.titulo