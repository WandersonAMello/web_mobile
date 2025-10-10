# -*- coding: utf-8 -*-
from django.forms import ModelForm
from anuncio.models import Anuncio

class FormularioAnuncio(ModelForm):
    class Meta:
        model = Anuncio
        exclude = [] #campos a serem excluídos do formulário