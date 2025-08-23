from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('vacancies/', views.vacancies, name='vacancies'), # Список вакансий
    path('candidates/', views.candidates, name='candidates'), # Список кандидатов
    path('dashboard/', views.dashboard, name='dashboard'), # личный кабинет
    path('user_edit/', views.user_edit, name='user_edit'), # редактирование профиля пользователя
    path('templates/', views.templates, name='templates'), # список писем
    path('candidates/<int:pk>/', views.candidate_detail, name='candidate_detail'), # детали по конкретному кандидату
    path('login/', views.user_login, name='login'), # вход
    path('logout/', views.user_logout, name='logout'), # выход
    path('vacancy_create/', views.vacancy_create, name='vacancy_create'), # создание вакансии
    path('vacancy_edit/<int:pk>/', views.vacancy_edit, name='vacancy_edit'), # редактирование конкретной вакансии
    path('vacancy_detail/<int:pk>/', views.vacancy_detail, name='vacancy_detail'), # детали по конкретной вакансии
    path('vacancy_delete/<int:pk>/', views.vacancy_delete, name='vacancy_delete'),  # удаление кандидата
    path('vacancies/<int:vacancy_id>/send_emails/', views.send_vacancy_emails, name='send_vacancy_emails'), # отправка писем по вакансии
    path('template_create/', views.template_create, name='template_create'), # Создание шаблона письмак
    path('template_edit/<int:pk>', views.template_edit, name='template_edit'), # редактирование письма
    path('template_detail/<int:pk>/', views.template_detail, name='template_detail'), # детали по конкретнму письму
    path('template_delete/<int:pk>/', views.template_delete, name='template_delete'),  # удаление кандидата
    path('candidate_create/', views.candidate_create, name='candidate_create'), # создание карточки кандидата
    path('candidates/candidates_upload/', views.candidates_upload, name='candidates_upload'), # загрузка списка кандидатов
    path('candidate_edit/<int:pk>/', views.candidate_edit, name='candidate_edit'),  # редактирование карточки кандидата
    path('candidate_detail/<int:pk>/', views.candidate_detail, name='candidate_detail'),  # детали по кандидату
    path('candidate_delete/<int:pk>/', views.candidate_delete, name='candidate_delete'),  # удаление кандидата
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # обработка загружаемых файлов

