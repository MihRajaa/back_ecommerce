from rest_framework import serializers

from .models import *


# Serializations des tables

# Serializations de Gouvernat
class GouvernatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gouvernat
        fields = ['gouvernat', 'code_iso', 'index_code_postal', 'coordonnees']


# Serializations de Ville
class VilleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ville
        fields = ['ville', 'code_poste']


# Serializations de code de poste
class CodePosteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CodePoste
        fields = ['code_poste']


# Serializations d'Localite
class LocaliteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Localite
        fields = "__all__"


# Serializations d'adresse
class AdresseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Adresse
        fields = "__all__"
