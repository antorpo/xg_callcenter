from django.shortcuts import render
from django.http import JsonResponse, response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CadenaSerializer
from .models import Cadena

from .token_functions import historial_callcenter

# Obtener la ultima cadena ingresada
@api_view(['GET'])
def cadenaList(request):
	cadenas = Cadena.objects.all().order_by('-id')
	serializer = CadenaSerializer(cadenas, many=True)
	return Response(serializer.data)

# Crear cadenas
@api_view(['POST'])
def cadenaCreate(request):
	serializer = CadenaSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def cadenaDeleteAll(request):
	cadena = Cadena.objects.all()
	cadena.delete()

	return Response('Item succesfully delete!')


@api_view(['GET'])
def historialPuntaje(request):
	cadena = Cadena.objects.first()
	response = historial_callcenter.historialJson(cadena.secuencia)
	return Response(response)