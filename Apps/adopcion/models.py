from django.db import models

# Create your models here.

class Persona(models.Model):
    Cedula = models.IntegerField()
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=70)
    Edad = models.IntegerField()
    Telefono = models.CharField(max_length=12)
    Correo = models.EmailField()
    Domicilio = models.TextField()

    def Nombre_Adoptante(self):
        cadena = "{0} {1}"
        return cadena.format(self.Nombres, self.Apellidos)

    def __str__(self):
        return self.Nombre_Adoptante()

