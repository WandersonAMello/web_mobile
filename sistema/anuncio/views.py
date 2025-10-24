# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from anuncio.models import Anuncio
from anuncio.forms import FormularioAnuncio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import FileResponse, Http404
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.generics import ListAPIView, DestroyAPIView
from anuncio.serializers import SerializadorAnuncio
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

class ListarAnuncios(LoginRequiredMixin, ListView): #herda de LoginRequiredMixin para exigir autenticação
    """
    View para listar anúncios cadastrados.
    """
    model = Anuncio #parametro obrigatório
    context_object_name = 'lista_anuncios' #devine o nome do objeto no template
    template_name = 'anuncio/listar.html'

    def get_queryset(self):
        """ Retorna a lista de anúncios ativos."""
        #return Anuncio.objects.all() #para modificar o filtro, altere aqui
        return Anuncio.objects.filter(ativo=True) #exemplo de filtro para retornar apenas anúncios ativos


class CriarAnuncios(LoginRequiredMixin, CreateView):
    """
    View para criar um novo anúncio.
    """
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios') #redireciona para a lista de anúncios após criar um novo anúncio
    
class EditarAnuncios(LoginRequiredMixin, UpdateView):
    """
    View para editar um anúncio existente.
    """
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios') #redireciona para a lista de anúncios após editar um anúncio

class DeletarAnuncios(LoginRequiredMixin, DeleteView):
    """
    View para deletar um anúncio existente.
    """
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios') #redireciona para a lista de anúncios após deletar um anúncio
    
class APIListarAnuncios(ListAPIView):
    """
    View para listar instâncias de anúncios (por meio da API REST).
    """
    serializer_class = SerializadorAnuncio
    
    def get_queryset(self):
        return Anuncio.objects.all()