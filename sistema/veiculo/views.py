# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class ListarVeiculos(LoginRequiredMixin, ListView): #herda de LoginRequiredMixin para exigir autenticação
    """
    View para listar veiculos cadastrados.
    """
    model = Veiculo #parametro obrigatório
    context_object_name = 'lista_veiculos' #devine o nome do objeto no template
    template_name = 'veiculo/listar.html'

    def get_queryset(self):
        """ Retorna a lista de veículos do ano atual."""
        return Veiculo.objects.all() #para modificar o filtro, altere aqui


class CriarVeiculos(LoginRequiredMixin, CreateView):
    """
    View para criar um novo veículo.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos') #redireciona para a lista de veículos após criar um novo veículo