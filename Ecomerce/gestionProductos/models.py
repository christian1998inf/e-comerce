from django.db import models

# Create your models here.

class Producto(models.Model):
    Id_Producto=models.IntegerField()
    Nombre=models.CharField(max_length=30)
    Stock=models.IntegerField()
    Precio=models.IntegerField()


class Pedidos(models.Model):
    Id_Pedido=models.IntegerField()
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    Correo=models.EmailField()
    Telefono=models.IntegerField
    Fecha=models.DateField()
    Entregado=models.BooleanField()
    Comentario=models.CharField(max_length=300)