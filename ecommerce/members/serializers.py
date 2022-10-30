from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import *


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=MyUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'password2', 'email', 'firstname',
                  'lastname', 'date_of_birth', 'phone', 'password', 'is_active')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = MyUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname']
        )
        user.set_password(user.password)
        user.save()
        return user


class MyUserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class UserAdressSerialiser(serializers.ModelSerializer):
    class Meta:
        model = UserAdress
        fields = '__all__'
