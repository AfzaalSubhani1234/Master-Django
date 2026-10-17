from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )
    confirm_password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "confirm_password",
        ]
        read_only_fields = ["id"]

    def validate(self, data):
        password = data["password"]

        if password != data["confirm_password"]:
            raise serializers.ValidationError({
                "confirm_password": "Passwords do not match."
            })

        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError({
                "password": "Password must contain at least one number."
            })

        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        return User.objects.create_user(**validated_data)


