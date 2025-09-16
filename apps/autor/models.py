from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    