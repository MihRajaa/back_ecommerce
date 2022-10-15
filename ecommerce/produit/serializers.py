from rest_framework import serializers

from .models import Categorie, Produit


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
