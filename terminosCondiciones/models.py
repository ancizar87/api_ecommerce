from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class TerminosCondiciones(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=50)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name = "TerminosCondiciones"
        verbose_name_plural = "TerminosCondiciones"
        ordering = ['-id']
        
    def __str__(self):
        return self.title