from django.db import models
from usuarios.models import CustomUser

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    estado_choice = [
        ('Excelente', 'Excelente'),
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('Malo', 'Malo'),
    ]
    estado = models.CharField(max_length=255, choices=estado_choice)
    vendedor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='productos')
