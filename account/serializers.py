from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    EmailField,
)

from account.models import DriverUser


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(
        min_length=4,
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    email = EmailField(label='Email address')

    class Meta:
        model = DriverUser
        fields = [
            'id',
            'username',
            'password',
            'email',
        ]

    extra_kwargs = {"password":
                        {"write_only": True},
                    "id":
                        {"read_only": True}
                    }

    def validate(self, data):
        return data

    def validate_email(self, value):
        email = value
        user_qs = DriverUser.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("Email already registered")
        return value

    def validate_username(self, value):
        username = value
        user_qs = DriverUser.objects.filter(username=username)
        if user_qs.exists():
            raise ValidationError("Username already existed")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user_obj = DriverUser(
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj
