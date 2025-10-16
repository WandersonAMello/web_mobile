from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from veiculo.models import *
from veiculo.forms import *

class TestesModelVeiculo(TestCase):
    '''
    Classe de testes para o model Veiculo
    '''
    def setUp(self): #não é um teste, mas sim uma preparação para os testes
        '''
        Configura o ambiente de teste criando uma instância do modelo Veiculo.
        '''
        #para cada teste um novo banco de dados é criado
        #e destruído ao final do teste
        self.instancia = Veiculo(
            marca=1,
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )
        
    def test_is_new(self): #método que inicia com test_ é um teste
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = datetime.now().year - 5
        self.assertFalse(self.instancia.veiculo_novo)
        
    def test_years_of_use(self):
        self.instancia.ano = datetime.now().year - 10
        self.assertEqual(self.instancia.anos_de_uso(), 10)

class TestesViewListarVeiculos(TestCase):
    '''
    Classe de testes para a view ListarVeiculos
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('listar-veiculos')
        Veiculo(marca=1, modelo='ABCDE', ano=2020, cor=1, combustivel=4).save()
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('lista_veiculos')), 1)
        
class TestesViewCriarVeiculos(TestCase):
    '''
    Classe de testes para a view CriarVeiculos
    '''
    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculos')
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo) #verifica se o form é uma instância de FormularioVeiculo
        
    def test_post(self):
        dados = {
            'marca': 2,
            'modelo': 'ABCDE',
            'ano': 2023,
            'cor': 3,
            'combustivel': 1
        }
        response = self.client.post(self.url, dados)
        
        #verifica se apos a insercao houve um redirecionamento para a lista de veiculos
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'ABCDE')

