from django.shortcuts import render
from django.http import HttpResponse
import datetime 

# Create your views here.

def displayDateTime(request):
    dt= datetime.datetime.now()
    s = "<b>La fecha y hora es: </b>"+str(dt)
    return HttpResponse(s)

