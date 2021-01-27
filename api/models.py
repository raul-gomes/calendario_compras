from django.db import models
from dateutil import relativedelta


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

    @property
    def valor_parcela(self):
        valor_parcelado = (self.valor_compra - self.entrada) / self.quantidade_parcelas
        return valor_parcelado

    def data_parcelas(self):
        nextMonth = self.data_compra
        parcelas_info = {}
        datas = []
        for x in range(1, self.quantidade_parcelas + 1):
            parcelas_info[x] = nextMonth
            nextMonth = nextMonth + relativedelta.relativedelta(months=1)
            datas.append(nextMonth)
        return datas
