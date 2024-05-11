class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def serialize(self):
    return self.__dict__