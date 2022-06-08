from django.db import models

# Create your models here.
# Modelo para la categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")



    def __str__(self):
        return self.nombreCategoria

# modelo para el Producto
class Producto(models.Model):
    Id= models.CharField(max_length=6, primary_key=True, verbose_name='Id producto')
    Nombre = models.CharField(max_length=20, verbose_name='Nombre')
    Descripcion =  models.CharField(max_length=200, verbose_name='Descripcion')
    Precio =  models.CharField(max_length=200, null=True, blank=True, verbose_name='Precio')
    Stock = models.CharField(max_length=7, verbose_name='Stock')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.Id
