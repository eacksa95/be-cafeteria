from rest_framework import serializers
from .models import Pedido
import json

class PedidoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'mesa', 'lista_productos', 'monto', 'estado']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lista_productos'] = json.loads(representation['lista_productos'])
        return representation
    