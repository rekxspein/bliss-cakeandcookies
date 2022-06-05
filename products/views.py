from urllib import request
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product, ProductCategory
from products.serializers import ProductSerializer, ProductCategorySerializer

# Get all users


@api_view(['GET', 'POST'])
def getProducts(request, id=None):
    if request.method == 'GET':
        if id:
            product = Product.objects.filter(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        
        products = Product.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
