from django.db import models

class Institucion(models.Model):
    nombreInstitucion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreInstitucion

class Curso(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    grado = models.CharField(max_length=50)
    numero = models.IntegerField()
    año = models.IntegerField()

    def __str__(self):
        return f"{self.grado} - {self.numero}"

class Estudiante(models.Model):
    nombreEstudiante = models.CharField(max_length=100)
    codigoEstudiante = models.CharField(max_length=50)
    cursoEstudiante = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreEstudiante

class CronogramaEstudiante(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class CronogramaBase(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Descuento(models.Model):
    tipoDescuento = models.CharField(max_length=50)

    def __str__(self):
        return self.tipoDescuento
