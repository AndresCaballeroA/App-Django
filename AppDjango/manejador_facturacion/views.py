from django.shortcuts import render
from .models import Factura

def listar_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'manejador_facturacion/listar.html', {'facturas': facturas})
