from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Link for the main page
    path('about/', views.about, name= 'about'), # Link for the page 'About'
]