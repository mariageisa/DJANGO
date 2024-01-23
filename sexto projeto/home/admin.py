from django.contrib import admin
from .models import Paragrafo

class texto (admin.ModelAdmin):
    texto_paragrafos = ('texto1', 'texto2')
admin.site.register(Produto, ListProduto)