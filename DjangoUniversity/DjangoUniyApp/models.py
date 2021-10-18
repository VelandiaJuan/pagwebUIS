from django.db import models

# Create your models here.
class Student(models.Model):
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50) 
    codigo = models.CharField(max_length=50) 
    telefono = models.CharField(max_length=50) 
    carrera = models.CharField(max_length=50) 
    deporte = models.CharField(max_length=50) 
    email = models.EmailField()
