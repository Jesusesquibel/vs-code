from django.db import models

# Create your models here.

"""Se genera una clase para llamar la tabla de la base de datos"""
class Clientes(models.Model):  
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()   #EmaiField ayuda a que se agregue correctamente el correo 
    tfno=models.CharField(max_length=10)
    
class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
        