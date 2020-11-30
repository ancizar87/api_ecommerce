from django.contrib import admin
from unidadMedida.models import UnidadM

# Register your models here.
class UnidadMAdmin(admin.ModelAdmin):
    model = UnidadM
    readonly_fields = ('created','updated')
    
admin.site.register(UnidadM, UnidadMAdmin)