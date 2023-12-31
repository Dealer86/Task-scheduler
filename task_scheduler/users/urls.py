from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('register/', views.user_register, name='user-register'),
    path('logout/', views.user_logout, name='user-logout'),
]
