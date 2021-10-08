# importando httpResponse e JsonResponse
from django.http import HttpResponse, JsonResponse
# importando o decorator csrf_exempt
from django.views.decorators.csrf import csrf_exempt
# importanto o json parse
from rest_framework.parsers import JSONParser
# importando model produto
from app.models import Produto
# importando serializador de produto
from app.serializer import ProdutoSerializer

# removendo o csrf
@csrf_exempt
# função list que contém o getAll e o Create
def produto_list(request):
  if request.method == 'GET':
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ProdutoSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
# função detail que recebe contém GET, PUT e DELETE
# necessitando da passagem do parámetro ID
def produto_detail(request, pk):

  # verificando ser o produto existe via id
  try:
    produto = Produto.objects.get(pk=pk)
  except Produto.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = ProdutoSerializer(produto)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = ProdutoSerializer(produto, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.erros, status=400)

  elif request.method == 'DELETE':
    produto.delete()
    return HttpResponse(status=204)