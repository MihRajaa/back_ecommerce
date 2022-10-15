from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ProduitSerializer
from .models import Produit
# Create your views here.


class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
