from django.db import models
from apps.autor.models import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_publicacion = models.DateField()
    paginas = models.IntegerField()
    disponible = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo