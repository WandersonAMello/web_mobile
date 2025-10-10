from django.db import models
from veiculo.consts import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEIS


class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)
    foto = models.ImageField(upload_to='veiculo/fotos', blank=True, null=True)
    
    def __str__(self):
        """
        Retorna uma representação legível do veículo.
        """
        return f"{self.get_marca_display()} {self.modelo} ({self.ano})"
    
    def get_marca_display(self):
        """
        Retorna o nome da marca do veículo.
        """
        return dict(OPCOES_MARCAS).get(self.marca, "Desconhecida")
