from django.urls import path
from . import views

urlpatterns = [
    #to get user information
    path('', views.getOrders),
]
