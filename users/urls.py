from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    #to get user information
    path('', views.get_user),

    #to login
    path('login/', views.login),

    #to register
    path('register/', views.register),
    
    #to logout single session (token)

    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),

    #to logout all sessions (token)
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    
    #to get address of a specific user
    path('address/', views.address),
]
