from django.db import models

# Create your models here.

class UnidadM(models.Model):
    medida = models.CharField(verbose_name="Unidad de medida", max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medida"
        ordering = ['-created']
        
    def __str__(self):
        return self.medida
