from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.templates, name='templates'),  # список писем
    path('template_create/', views.template_create, name='template_create'),  # Создание шаблона письмак
    path('template_edit/<int:pk>', views.template_edit, name='template_edit'),  # редактирование письма
    path('template_detail/<int:pk>/', views.template_detail, name='template_detail'),  # детали по конкретнму письму
    path('template_delete/<int:pk>/', views.template_delete, name='template_delete'),  # удаление письма
]