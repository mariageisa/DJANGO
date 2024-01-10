

from django.shortcuts import render
from django.http import HttpResponse #moddulo

def home(request):
    return render(request, 'home/index.html')

