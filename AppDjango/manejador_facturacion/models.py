from django.db import models
class Factura(models.Model):
    estudiante = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateField()

    def __str__(self):
        return f"Factura de {self.estudiante} por {self.monto}"
