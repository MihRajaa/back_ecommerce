from rest_framework import serializers

from .models import *


class MyUserSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'firstname', 'lastname',
                  'date_of_birth', 'phone', 'password', 'is_active', 'is_admin']


class UserAdresseSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAdress
        fields = ['user', 'adresse', 'adresse_type', 'active']
