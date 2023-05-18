from djongo import models

class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.CharField(max_length=100, default='cliente')
    mesa=models.IntegerField()
    lista_productos = models.JSONField()
    monto = models.IntegerField( default=0)
    estado = models.BooleanField(default=False)