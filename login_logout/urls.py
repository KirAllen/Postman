from django.urls import path
from . import views

urlpatterns = [
    path('in/', views.user_login, name='login'), # вход
    path('out/', views.user_logout, name='logout'), # выход
]