from django.db import models

class DetalleCobroEstudiante(models.Model):
    mes = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fechaCausacion = models.DateField()
    fechaLimite = models.DateField()
    frecuencia = models.CharField(max_length=50)

    def __str__(self):
        return f"Estudiante Cobro {self.mes} - {self.valor}"


class DetalleCobroCurso(models.Model):
    mes = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fechaCausacion = models.DateField()
    fechaLimite = models.DateField()

    def __str__(self):
        return f"Curso Cobro {self.mes} - {self.valor}"
