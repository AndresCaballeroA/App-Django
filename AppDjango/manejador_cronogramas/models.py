# models.py en manejador_cronogramas
from django.db import models

class Cronograma(models.Model):
    curso = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Cronograma de {self.curso}"
