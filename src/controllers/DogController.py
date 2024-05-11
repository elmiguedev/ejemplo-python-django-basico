from django.http import JsonResponse
from src.models.Dog import Dog
from ..repositories import DogRepository

def getDogs(request):
  dogs = DogRepository.getDogs()
  respose = []

  for dog in dogs:
    respose.append(dog.serialize())

  return JsonResponse(respose, safe=False)

def getDog(request, id):
  dog = DogRepository.getDog(id)
  return JsonResponse(dog.serialize(), safe=False)
