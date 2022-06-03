from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers, validators

from users.models import UserAddress


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), f"A user with that email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )
        return user

#UserAddress Serializer
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    # customer_address = UserAddressSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ("id","username", "email", "first_name", "last_name")

