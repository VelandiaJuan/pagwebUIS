from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return HttpResponse("Listado de estudiantes")


# Create your views here.
