from django.db import models

class Productos(models.Model):
    codigo=models.CharField(max_length=10, unique=True,blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    precio_costo = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    stock_inicial = models.IntegerField()

    def __str__(self):
        return self.nombre