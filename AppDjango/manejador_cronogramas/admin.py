from django.contrib import admin
from .models import Institucion, Curso, Estudiante, CronogramaEstudiante, CronogramaBase, Descuento

admin.site.register(Institucion)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(CronogramaEstudiante)
admin.site.register(CronogramaBase)
admin.site.register(Descuento)
