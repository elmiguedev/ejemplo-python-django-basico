from django.http import JsonResponse
from ..repositories import ProductoRepository

def getProductos(request):
  productos = ProductoRepository.getProductos()
  response = []
  for producto in productos:
    response.append(producto.serialize())
  return JsonResponse(productos, safe=False)