from rest_framework import serializers
from .models import Anuncio

class SerializadorAnuncio(serializers.ModelSerializer):
    """
    Serializador para o model Anuncio
    
    """
    
    class Meta:
        model = Anuncio
        exclude = []