from django.db import models


# Create your models here.
class Compras(models.Model):
    nome_compra = models.CharField(max_length=200)
    valor_compra = models.FloatField()
    entrada = models.FloatField()
    data_compra = models.DateField()
    tipo_parcelamento = models.IntegerField()
    quantidade_parcelas = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_compra
