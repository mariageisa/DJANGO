from django.db import models

class Livro(models.Model):
    nome_livro = models.CharField(max_length=100)
    ano_da_pub = models.IntegerField(max_length=4)
    qtd_de_pgn = models.IntegerField(max_length=100)
    nome_do_autor = models.CharField(max_length=50)
    nome_da_editora = models.CharField(max_length=50)
    preco = models.FloatField(max_length=100)

    def __str__ (self):
        return self.nome_livro



