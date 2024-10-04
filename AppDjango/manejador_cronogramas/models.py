# models.py en manejador_cronogramas
from django.db import models

class Cronograma(models.Model):
    curso = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Cronograma de {self.curso}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    cedula = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class DetalleCobroCurso(models.Model):
    mes = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField()


    def __str__(self):
        return self.curso.nombre


class CronogramaBase(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    detalle_cobro = models.ForeignKey(DetalleCobroCurso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estudiantes = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    cronograma = models.ForeignKey(CronogramaBase, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField()
    cursos = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
