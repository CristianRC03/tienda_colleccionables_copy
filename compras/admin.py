from django.contrib import admin
from .models import Carrito, Pedido, ItemCarrito

# Register your models here.
admin.site.register(Carrito)
admin.site.register(Pedido)
admin.site.register(ItemCarrito)