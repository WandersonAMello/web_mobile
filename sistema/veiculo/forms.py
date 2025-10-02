# -*- coding: utf-8 -*-
from django.forms import ModelForm
from veiculo.models import Veiculo

class FormularioVeiculo(ModelForm):
    """
    Formulário para o model Veiculo.
    """
    class Meta:
        model = Veiculo
        exclude = [] #campos a serem excluídos do formulário
        