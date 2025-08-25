from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserEditForm

# личный кабинет
@login_required
def dashboard(request):
    return render(request, 'user_profile/dashboard.html')


# Редактирование карточки пользователя
@login_required
def user_edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserEditForm(instance=user)
        return render(request, 'user_profile/user_edit.html', {'form': form, 'editing': True})
