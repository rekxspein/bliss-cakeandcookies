from django.urls import path
from . import views

urlpatterns = [
    # to get user information
    path('', views.getOrders),
    # to get order information
    path('<int:id>/', views.getOrder),
]
