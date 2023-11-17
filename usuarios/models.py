from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    cp = models.CharField(max_length=10)
    calle = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    foto_identificacion = models.CharField(max_length=255)
    roles = models.ManyToManyField(Group, related_name='usuarios_roles')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')

class Resena(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resenasUsuario')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='resenasProducto')
    valoracion = models.IntegerField()
    comentario = models.TextField()
    fecha_reseña = models.DateField(auto_now_add=True)
