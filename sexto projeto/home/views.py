
from django.shortcuts import render
from django.http import HttpResponse #moddulo

def home(request):
    texto1 = Paragrafo.objects.all()
#estrutura context 
    context = {
        'produtos':texto1,
    }
    
    return render(request, 'home/index.html')

