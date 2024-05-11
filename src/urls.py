from django.urls import path
from .controllers.DogController import getDogs, getDog
from .controllers.ProductoController import getProductos

urlpatterns = [
  path("dogs/", getDogs),
  path("dogs/<int:id>/", getDog),
  path("productos/", getProductos)
]


