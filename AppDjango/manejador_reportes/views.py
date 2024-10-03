from django.shortcuts import render
from .models import Reporte

def generar_reporte(request):
    # Lógica para generar reportes aquí
    reportes = Reporte.objects.all()
    return render(request, 'manejador_reportes/listar.html', {'reportes': reportes})

from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la aplicación")
