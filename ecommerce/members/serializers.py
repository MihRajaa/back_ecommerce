from rest_framework import serializers

from .models import *


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'password', 'firstname', 'email',
                  'lastname', 'date_of_birth', 'phone', 'password', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True},
        }

        def create(self, validated_data):
            user = MyUser.objects.create_user(username=validated_data['username'],     password=validated_data['password'],
                                              first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
            return user


class MyUserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class UserAdresseSerialiser(serializers.ModelSerializer):
    class Meta:
        model = UserAdress
        fields = '__all__'
