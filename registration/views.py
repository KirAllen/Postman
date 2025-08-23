from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages


# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
