from rest_framework import serializers
from .models import Compras


class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = [
                    'id',
                    'nome_compra',
                    'valor_compra',
                    'entrada',
                    'data_compra',
                    'tipo_parcelamento',
                    'quantidade_parcelas',

                ]