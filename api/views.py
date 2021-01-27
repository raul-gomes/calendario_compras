from django.shortcuts import render
from rest_framework import viewsets
from .models import Compras
from .serializers import ComprasSerializer


class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer
