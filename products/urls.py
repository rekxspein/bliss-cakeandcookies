from django.urls import path
from . import views

urlpatterns = [
    #to get user information
    path('', views.getProducts),
    path('<int:id>/', views.getProducts),
    path('productbycategory/<int:id>/', views.getProductsByCategory),
    path('categories/', views.getProductCategories),
    path('categories/<int:id>', views.getProductCategories),
]
