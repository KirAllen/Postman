from django.urls import path
import registration.views as views

urlpatterns = [
    path('', views.register, name='register'),  # регистрация нового пользователя
]


