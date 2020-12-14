from django.contrib import admin
from productos.models import Producto
from caractproducto.models import Caracteristica

# Register your models here.

class CaracteristicaInline(admin.TabularInline):
    model = Caracteristica


    
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    inlines = [CaracteristicaInline]
  
admin.site.register(Producto, ProductoAdmin)