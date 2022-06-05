from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    #to get user information
    path('products/', views.getProducts),
]
