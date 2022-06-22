from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers, validators

from products.models import ProductCategory, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# class ProductnameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('name',)
#