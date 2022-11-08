from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliares.models import familiares
from django.template import loader
# Create your views here.

def vista_familiares(request):
    familiar1= familiares(nombre="Gustavo",apellido="Sassi",edad="56",cumpleanios="1966-07-11")
    familiar2= familiares(nombre="Maria",apellido="Menna",edad="54",cumpleanios="1967-11-08")
    familiar3= familiares(nombre="Emilia",apellido="Sassi",edad="22",cumpleanios="2000-08-26")
    return render(request,'desafio.html',{'familia':[familiar1,familiar2,familiar3]})
    