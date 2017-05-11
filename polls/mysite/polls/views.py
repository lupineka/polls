from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detalles(request, pregunta_id):
    return HttpResponse("lupita lupita lupita lupita")

def resultados(request, pregunta_id):
    response = "Estas buscando los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Haz votado en la pregunta %s." % pregunta_id)