from django import forms
from django.core.exceptions import ValidationError

CHOICES = [(0, 'Diário'), (1, 'Quinzenal'), (2, 'Mensal')]


def numero_positvo(valor):
    if valor < 0:
        raise ValidationError('Valor deve ser maior que zero')


def valida_entrada(entrada):
    if entrada > ComprasForm.valor:
        raise ValidationError('O valor de entrada deve ser inferior ao valor da compra.')


class ComprasForm(forms.Form):
    nome_compra = forms.CharField(label='Descrição')
    valor_compra = forms.FloatField(label='Valor da compra', validators=[numero_positvo])
    entrada = forms.FloatField(label='Entrada', validators=[numero_positvo])
    data_compra = forms.DateField(label='Data da compra')
    tipo_parcelamento = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        label='Forma de Parcelamento'
    )
    quantidade_parcelas = forms.IntegerField(label='Quantas parcelas', validators=[numero_positvo])


