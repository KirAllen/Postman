from django.shortcuts import render

# Главная страница
def index(request):
    return render(request, 'main/index.html')


# Страница про нас
def about(request):
    return render(request, 'main/about.html')

