from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def holaHora(request):
    dt = datetime.datetime.now()
    s = "<h1>Hola Wapisimos</h1><br><b>Fecha: </b>"+str(dt)
    return HttpResponse(s)
