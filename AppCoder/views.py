from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso


def curso_creado(request, camada):
    curso = Curso(nombre='HTML' , camada=camada)
    curso.save()
    
    return HttpResponse(f'curso de HTML:  {camada}')