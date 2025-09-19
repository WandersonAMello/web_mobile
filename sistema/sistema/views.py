# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

class Login(View):
    """
    Class-based view para autenticação de usuários.
    """
    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)
    
    def post(self, request):
        
        # Obtém as credenciais do formulário
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)
        
        # Verifica se as credenciais são válidas
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            
            #verifica se o usuário está ativo no sistema
            if user.is_active:
                login(request, user)
                return redirect('/veiculo')  # Redireciona para a página de veículos após o login bem-sucedido

            
        return render(request, 'autenticacao.html', {'mensagem': 'Login invalido!'})