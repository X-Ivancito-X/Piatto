from django.db import models

# Create your models here.

class Usuarios(models.Model):
    IdUsuario=models.AutoField(primary_key=True)
    Usuario=models.TextField(max_length=20)
    Email=models.TextField(max_length=128)
    Contraseña=models.TextField(max_length=16)
    Tipo=models.TextField()

    def __int__(self):
        self.IdUsuario

class Productos(models.Model):
    IdProducto=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=50)
    Tipo=models.TextField(max_length=10)
    Descripcion=models.TextField(max_length=64)
    Imagen=models.ImageField(upload_to="Productos",null=True)

    def __int__(self):
        self.IdProducto
