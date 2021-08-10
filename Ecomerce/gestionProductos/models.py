from django.db import models

# Create your models here.
#class Usuario(models.Model):

<<<<<<< HEAD
=======

#class Seccion(models.Model):


#class Pedidos(models.Model):


#class Stock(models.Model):


#class Fecha(models.Model):
>>>>>>> origin/solange-rama
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
<<<<<<< HEAD
    Comentario=models.CharField(max_length=300)
=======
    Comentario=models.CharField(max_length=300)


    
>>>>>>> origin/solange-rama
