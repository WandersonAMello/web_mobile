# -*- coding: utf-8 -*-

from django.urls import path
from anuncio.views import *

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'), #rota para listar anúncios
    path('novo/', CriarAnuncios.as_view(), name='criar-anuncios'), #rota para criar um novo anúncio
    path('editar/<int:pk>/', EditarAnuncios.as_view(), name='editar-anuncios'), #rota para editar um anúncio
    path('deletar/<int:pk>/', DeletarAnuncios.as_view(), name='deletar-anuncios'), #rota para deletar um anúncio
]