from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers, validators

from orders.models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 1


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'