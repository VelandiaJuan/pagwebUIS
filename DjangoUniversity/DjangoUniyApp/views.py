from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    estudiantes = Student.objects.all()
    context = {'clase': 'UIS se ejercita','estudiantes':estudiantes}
    return render(request,'student_list.html',context) 


# Create your views here.
