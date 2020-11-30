from django.contrib import admin
from servicios.models import Servicio
from galleryServices.models import Images

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Images

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    inlines = [ImageInline,]
  
admin.site.register(Servicio, ServicioAdmin)