from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers, validators

from orders.models import Order, OrderItem
# from products.serializers import ProductnameSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductnameSerializer()

    # product is the name of the field in the OrderItem model
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ('id', 'product_name', 'quantity', 'price', 'item_total')


class OrderSerializer(serializers.ModelSerializer):

    first_name = serializers.ReadOnlyField(source='address.first_name')
    last_name = serializers.ReadOnlyField(source='address.last_name')
    address = serializers.ReadOnlyField(source='address.address')
    city = serializers.ReadOnlyField(source='address.city')
    state = serializers.ReadOnlyField(source='address.state')
    postal_code = serializers.ReadOnlyField(source='address.postal_code')
    mobile = serializers.ReadOnlyField(source='address.mobile')

    orders_item = OrderItemSerializer(many=True)  # a field from OrderItem Model using related_name

    class Meta:
        model = Order
        fields = ('id', 'order_id', 'status', 'first_name',
                  'last_name', 'address', 'city', 'state', 'mobile', 'postal_code', 'orders_item', 'total_amount')
