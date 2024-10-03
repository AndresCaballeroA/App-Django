from django.db import models

class Reporte(models.Model):
    curso = models.CharField(max_length=100)
    deuda_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reporte de {self.curso}"
