from django.contrib import admin
from productos.models import Producto
from caractproducto.models import Caracteristica
from galleryProducts.models import Imagenes

# Register your models here.

class CaracteristicaInline(admin.TabularInline):
    model = Caracteristica

class ImagenesInline(admin.TabularInline):
    model = Imagenes
    
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    inlines = [CaracteristicaInline, ImagenesInline]
  
admin.site.register(Producto, ProductoAdmin)