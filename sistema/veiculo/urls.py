# -*- coding: utf-8 -*-

from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'), #rota para listar veículos
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos') #rota para criar um novo veículo
]
