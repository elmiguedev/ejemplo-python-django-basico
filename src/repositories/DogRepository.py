from src.models.Dog import Dog
from ..utils.Connector import connection

def getDogs():
  connection.connect()
  cursor = connection.cursor()
  query = "select * from dog"
  cursor.execute(query)
  rows = cursor.fetchall()

  dogs = []

  for row in rows:
    dog = Dog(row[0], row[1])
    dogs.append(dog)

  cursor.close()
  return dogs

def getDog(id):
  connection.connect()
  cursor = connection.cursor()
  query = "select * from dog where id = %s"
  cursor.execute(query, (id,))
  row = cursor.fetchone()

  if (row == None):
    return None
  
  dog = Dog(row[0], row[1])
  cursor.close()
  return dog
