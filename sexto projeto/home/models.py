from django.db import models

class Paragrafos (models.Model):
    texto1 = models.TextField
    texto2 = models.TextField
    
def __str__(self):
    return self.texto1

