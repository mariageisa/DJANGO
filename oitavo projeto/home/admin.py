from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Livro

class ListLivros (admin.ModelAdmin):
    list_display = ('nome_livro', 'ano_da_pub', 'qtd_de_pgn', 'nome_do_autor', 'nome_da_editora', 'preco')

admin.site.register(Livro, ListLivros) 