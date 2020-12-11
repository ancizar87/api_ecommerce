from django.db import models

# Create your models here.

class Ramal(models.Model):
    nombre = models.CharField(verbose_name="Nombre", blank=False, null=False, max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name = "Ramal"
        verbose_name_plural = "Ramales"
        ordering = ['id']
        
    def __str__(self):
        return self.nombre
    
