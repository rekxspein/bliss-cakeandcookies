import json
import re
from urllib import request
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.models import Order, OrderItem, UserAddress

from orders.serializers import OrderItemSerializer, OrderSerializer
from products.models import Product

# # Create your views here.
# custome_data = [{"data": {
#     "id": 1,
#     "name": "John",
#     "age": 30
# }}]


@api_view(['GET', 'POST'])
def getOrders(request):
    currentUser = request.user
    if currentUser.is_authenticated:
        if request.method == 'GET':
            order = Order.objects.filter(user=currentUser)
            data = OrderSerializer(order, many=True).data
            return Response(data)

        elif request.method == 'POST':
            data = request.data  # putting request data inside data
            currentAddress = UserAddress.objects.filter(
                id=data['address']).first()  # .create() need an actual Model instance, so calling it
            if not currentAddress:
                return Response({'error': 'User address not found'}, status=400)

            queryOrder = Order.objects.create(
                user=request.user, total_amount=data['total_amount'], address=currentAddress)
            queryOrder.save()

            # creating order items

            # currentOrder = Order.objects.filter(
            #     data['id']).first()
            # if not currentOrder:
            #     return Response({'error': 'User Order not found'}, status=400)

            for i in data["order_items"]:
                print(i)
                currentProduct = Product.objects.filter(
                    id=i['product']).first()

                if not currentProduct:
                    return Response({'error': 'Product not found'}, status=400)

                createOrderItems = OrderItem.objects.create(
                    order=queryOrder, product=currentProduct, quantity=i[
                        'quantity'], price=i['price'], item_total=i['item_total']
                )
                createOrderItems.save()

            return Response({'response': 'Order Added'}, status=201)
    return Response({'error': 'User is not authenticated'})


@api_view(['GET', 'POST'])
def getOrder(request, id=None):
    if request.method == 'GET':
        if id:
            print("id: ", id)
            order = Order.objects.all().filter(id=id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            return Response({'error': 'No id specified'})
