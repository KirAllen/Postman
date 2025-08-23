from django.contrib.auth.forms import AuthenticationForm
from django import forms


# Форма входа (логина)
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
