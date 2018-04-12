from django.db import models
from Apps.adopcion.models import Persona

# Create your models here.

class Vacuna(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.Nombre)

class Mascota(models.Model):
    Nombre = models.CharField(max_length=50)
    SEXOS = (('H', 'Hembra'), ('M', 'Macho'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    Edad_Aproximada = models.IntegerField()
    Fecha_Rescate = models.DateField()
    Persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    Vacuna = models.ManyToManyField(Vacuna, blank=True)


    def __str__(self):
        return "{0}".format(self.Nombre)

