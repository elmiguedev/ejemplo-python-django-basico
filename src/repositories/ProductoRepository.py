from src.models.Producto import Producto
from ..utils.Connector import connection

def getProductos():
  connection.connect()
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM productos")
  query = cursor.fetchall()
  productos = []
  for i in query:
      producto = Producto(i[0], i[1], i[2], i[3], i[4], i[6], i[5], i[7])
      productos.append(producto)
  return productos