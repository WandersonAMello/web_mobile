# -*- coding: utf-8 -*-

from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'), #rota para listar veículos
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'), #rota para criar um novo veículo
    path('editar/<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'), #rota para editar um veículo
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'), #rota para servir fotos de veículos
]
