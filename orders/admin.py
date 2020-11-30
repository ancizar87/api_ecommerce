from django.contrib import admin
from orders.models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    readonly_fields = ['producto','precio', 'cantidad']
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['usuario','estado', 'precio_total', 'invoice_no', 'fecha']
    list_display = ['usuario', 'estado', 'precio_total', 'invoice_no', 'fecha']
    list_filter = ['estado', 'fecha']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

    