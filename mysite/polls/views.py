from django.shortcuts import HttpResponse


def index(reuest):
    return HttpResponse("Hola, mundo. estas en el indice polls")

# Create your views here.
