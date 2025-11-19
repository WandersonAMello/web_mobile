# -*- coding: utf-8 -*-

from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'), #rota para listar veículos
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'), #rota para criar um novo veículo
    path('editar/<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'), #rota para editar um veículo
    path('deletar/<int:pk>/', DeletarVeiculos.as_view(), name='deletar-veiculos'), #rota para deletar um veículo
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'), #rota para servir fotos de veículos
    
    path('api/', APIListarVeiculos.as_view(), name='api-listar-veiculos'), #rota para listar veículos via API REST
    path('api/deletar/<int:pk>/', APIDeletarVeiculos.as_view(), name='api-deletar-veiculos'), #rota para deletar um veículo via API REST
]
