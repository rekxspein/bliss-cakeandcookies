from urllib import request
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product, ProductCategory
from products.serializers import ProductSerializer, ProductCategorySerializer

# Get all products if no id, and if id get the product with the id


@api_view(['GET', 'POST'])
def getProducts(request, id=None):
    if request.method == 'GET':
        if id:
            product = Product.objects.filter(id=id)
            serializer = ProductSerializer(
                product, context={"request": request})
            return Response(serializer.data)

        else:
            products = Product.get_all_products()
            serializer = ProductSerializer(
                products, many=True, context={"request": request})
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(
            data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


# get the product categories

@api_view(['GET', 'POST'])
def getProductCategories(request, id=None):
    if request.method == 'GET':
        if id:
            product_category = ProductCategory.objects.filter(id=id)
            serializer = ProductCategorySerializer(
                product_category, context={"request": request})
            return Response(serializer.data)

        else:
            product_categories = ProductCategory.get_all_product_categories()
            serializer = ProductCategorySerializer(
                product_categories, many=True, context={"request": request})
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductCategorySerializer(
            data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)


# get the products by category

@api_view(['GET', 'POST'])
def getProductsByCategory(request, id=None):
    if request.method == 'GET':
        if id:
            product = Product.objects.filter(category_id=id)
            serializer = ProductSerializer(
                product, many=True, context={"request": request})
            return Response(serializer.data)

        else:
            products = Product.get_all_products()
            serializer = ProductSerializer(
                products, many=True, context={"request": request})
            return Response(serializer.data)
