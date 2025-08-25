from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'), # личный кабинет
    path('user_edit/', views.user_edit, name='user_edit'), # редактирование профиля пользователя
]

