from django.db import models

class Anuncio(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    veiculo = models.ForeignKey('veiculo.Veiculo', on_delete=models.CASCADE) # Relacionamento com o modelo Veiculo para associar o anúncio a um veículo específico.

    def __str__(self):
        return self.titulo
    
