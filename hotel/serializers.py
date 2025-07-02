from rest_framework import serializers
from .models import User, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["uuid", "email", "name", "number", "is_active", "created_at", "updated_at"]
        read_only_fields = ["uuid", "created_at", "updated_at"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["uuid", "user", "item_name", "quantity", "status", "created_at", "updated_at"]
        read_only_fields = ["uuid", "created_at", "updated_at"]
