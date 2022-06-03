from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication

from users.models import UserAddress
from .serializers import RegisterSerializer, UserAddressSerializer, UserSerializer


def serialize_user(user):
    return {
        "id":user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": UserSerializer(user).data,
            "token": token
        })


@api_view(['GET'])
def get_user(request):
    user = request.user
    query1 = UserAddress.objects.filter(customer = user)
    if user.is_authenticated:
        return Response({
            'user_data': UserSerializer(user).data,
            'address': UserAddressSerializer(query1, many = True).data
        })
    return Response({'error': 'User is not authenticated'})

@api_view(['GET','POST','DELETE'])
def address(request):
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            query1 = UserAddress.objects.filter(customer = user)
            return Response({
                # 'user_data': UserSerializer(user).data,
                'address': UserAddressSerializer(query1, many = True).data
            })
        return Response({'error': 'User is not authenticated'})
    
    elif request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            serializer = UserAddressSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(customer = user)
                return Response({'success': 'Address added'})
        return Response({'error': 'User is not authenticated'})

    elif request.method == 'DELETE':
        user = request.user
        if user.is_authenticated:
            query1 = UserAddress.objects.filter(customer = user)
            query1.delete()
            return Response({'success': 'Address deleted'})
        return Response({'error': 'User is not authenticated'})
    
    elif request.method == 'PUT':
        user = request.user
        if user.is_authenticated:
            query1 = UserAddress.objects.filter(customer = user)
            serializer = UserAddressSerializer(query1, data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'success': 'Address updated'})
        return Response({'error': 'User is not authenticated'})
        
    return Response({'error': 'Method not allowed'})