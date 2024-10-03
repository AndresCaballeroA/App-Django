from manejador_facturacion.models import Factura

def generar_reporte_facturacion():
    facturas = Factura.objects.all()
    # Lógica para generar el reporte, por ejemplo, en CSV o PDF
    return facturas