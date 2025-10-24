from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

from anuncio.models import *
from anuncio.forms import *
from anuncio.views import *

from veiculo.models import *


class TestesModelAnuncio(TestCase):
    '''
    Classe de testes para o model Anuncio
    '''
    def setUp(self):
        '''
        Configura o ambiente de teste criando uma instância do modelo Anuncio.
        '''
        self.user = User.objects.create(username='teste', password='12345')
        self.veiculo = Veiculo.objects.create(
            marca=1,
            modelo='TesteModelo',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )
        self.anuncio = Anuncio(
            titulo='Anuncio Teste',
            descricao='Descrição do anúncio de teste',
            preco=10000.00,
            veiculo=self.veiculo
        )
        
    def test_str_representation(self):
        self.assertEqual(str(self.anuncio), 'Anuncio Teste')
        
    def test_default_ativo(self):
        self.assertTrue(self.anuncio.ativo)
        
class TestesViewListarAnuncios(TestCase):
    '''
    Classe de testes para a view ListarAnuncios
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('listar-anuncios')
        veiculo = Veiculo.objects.create(
            marca=1,
            modelo='TesteModelo',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )
        Anuncio.objects.create(
            titulo='Anuncio Teste',
            descricao='Descrição do anúncio de teste',
            preco=10000.00,
            veiculo=veiculo
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('lista_anuncios')), 1)

class TestesViewCriarAnuncios(TestCase):
    '''
    Classe de testes para a view CriarAnuncios
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar-anuncios')
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioAnuncio) #verifica se o form é uma instância de FormularioAnuncio
    
    def test_post(self):
        veiculo = Veiculo.objects.create(
            marca=1,
            modelo='TesteModelo',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )
        dados = {
            'titulo': 'Anuncio Teste',
            'descricao': 'Descrição do anúncio de teste',
            'preco': 15000.00,
            'veiculo': veiculo.id
        }
        response = self.client.post(self.url, dados)
        
        #verifica se apos a insercao houve um redirecionamento para a lista de anuncios
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-anuncios'))
        
        self.assertEqual(Anuncio.objects.count(), 1)
        self.assertEqual(Anuncio.objects.first().titulo, 'Anuncio Teste')
        
class TestesViewEditarAnuncios(TestCase):
    '''
    Classe de testes para a view EditarAnuncios
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('editar-anuncios', args=[1])
        veiculo = Veiculo.objects.create(
            marca=1,
            modelo='TesteModelo',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )
        self.anuncio = Anuncio.objects.create(
            titulo='Anuncio Teste',
            descricao='Descrição do anúncio de teste',
            preco=10000.00,
            veiculo=veiculo
        )
    
    def test_put(self):
        dados = {
            'titulo': 'Anuncio Teste Editado',
            'descricao': 'Descrição do anúncio de teste editado',
            'preco': 12000.00,
            'veiculo': self.anuncio.veiculo.id
        }
        response = self.client.post(self.url, dados)
        
        #verifica se apos a edicao houve um redirecionamento para a lista de anuncios
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-anuncios'))
        
        self.anuncio.refresh_from_db()
        self.assertEqual(self.anuncio.titulo, 'Anuncio Teste Editado')
        self.assertEqual(self.anuncio.preco, 12000.00)