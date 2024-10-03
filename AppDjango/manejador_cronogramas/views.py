from django.shortcuts import render

from .models import Cronograma

def listar_cronogramas(request):
    cronogramas = Cronograma.objects.all()
    return render(request, 'manejador_cronogramas/listar.html', {'cronogramas': cronogramas})

