from django.urls import path
from . import views

urlpatterns = [
    path('vacancies/', views.vacancies, name='vacancies'),  # Список вакансий
    path('vacancy_create/', views.vacancy_create, name='vacancy_create'),  # создание вакансии
    path('vacancy_edit/<int:pk>/', views.vacancy_edit, name='vacancy_edit'),  # редактирование конкретной вакансии
    path('vacancy_detail/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),  # детали по конкретной вакансии
    path('vacancy_delete/<int:pk>/', views.vacancy_delete, name='vacancy_delete'),  # удаление вакансии
    path('vacancies/<int:vacancy_id>/send_emails/', views.send_vacancy_emails, name='send_vacancy_emails'), # отправка писем по вакансии
]