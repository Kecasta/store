from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Clientes(models.Model):
    nombre= models.CharField(max_length=50, blank=False,null=False)
    apellido= models.CharField(max_length=50, blank=False,null=False)
    contacto= models.IntegerField(max_length=20,blank=False, null=False)
    email= models.EmailField(max_length=254,blank=False, null=False)
    empresa=models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

