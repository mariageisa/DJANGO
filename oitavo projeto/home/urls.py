# CRIANDO MINHAS ROTAS
from django.urls import path
from . import views
# modulo     função

urlpatterns = [
    path('', views.home, name='home'),
]