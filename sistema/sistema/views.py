# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class Login(View):
    """
    Class-based view para autenticação de usuários.
    """
    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)