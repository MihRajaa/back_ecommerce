from rest_framework import serializers

from .models import *
# from django.contrib.auth.models import User


# Serializations des tables

# Serializations de Gouvernat
class GouvernatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gouvernat
        fields = ['gouvernat', 'code_iso', 'coordonnees']


# Serializations de Ville
class VilleSerializer(serializers.HyperlinkedModelSerializer):
    gouvernat = GouvernatSerializer(many=False)

    class Meta:
        model = Ville
        fields = ['name_ville', 'gouvernat']


# Serializations de code de poste
class CodePosteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CodePoste
        fields = ['code_poste']


# Serializations d'utilisateur
# class UserSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'is_active']
