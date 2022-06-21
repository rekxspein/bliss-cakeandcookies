import json
from urllib import request
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.models import Order, OrderItem

from orders.serializers import OrderItemSerializer, OrderSerializer

# # Create your views here.
# custome_data = [{"data": {
#     "id": 1,
#     "name": "John",
#     "age": 30
# }}]


@api_view(['GET', 'POST'])
def getOrders(request):
    userx = request.user
    if userx.is_authenticated:
        if request.method == 'GET':
            order = Order.objects.filter(user=userx)
            data = OrderSerializer(order, many=True).data
            return Response(data)

        elif request.method == 'POST':
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=201)
    return Response({'error': 'User is not authenticated'})


@api_view(['GET', 'POST'])
def getOrder(request, id=None):
    if request.method == 'GET':
        if id:
            print("id: ", id)
            order = Order.objects.all().filter(order_id=id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            return Response({'error': 'No id specified'})
