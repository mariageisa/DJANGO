from django.db import models
# regra padrao PASTA no plural e CLASSE no singular
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=30)
    sobrenome = models.CharField('sobrenome', max_length=30)
