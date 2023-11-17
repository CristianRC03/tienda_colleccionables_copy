from django.db import models

# Create your models here.
class Pago(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pagos')
    metodo_pago = models.CharField(max_length=255)
    fecha = models.DateField()