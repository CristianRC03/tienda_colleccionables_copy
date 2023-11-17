from django.db import models

# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='carritos')
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Pedido(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pedidos')
    detalle_pedido = models.OneToOneField(Carrito, on_delete=models.CASCADE, related_name='detalle_pedido')
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=255)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = (producto.precio * cantidad).decimal_places(2)