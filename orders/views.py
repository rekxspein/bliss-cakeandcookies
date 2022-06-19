from urllib import request
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.models import Order

from orders.serializers import OrderSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def getOrders(request, id=None):
    if request.method == 'GET':
        if id:
            order = Order.objects.filter(order_id=id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            orders = Order.get_all_orders()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

