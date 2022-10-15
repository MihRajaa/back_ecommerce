from rest_framework import serializers

from .models import *


# Serializations des tables

# Serializations de Gouvernat
class GouvernatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gouvernat
        fields = '__all__'


# Serializations de Ville
class VilleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ville
        fields = '__all__'


# Serializations de code de poste
class CodePosteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CodePoste
        fields = '__all__'


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
