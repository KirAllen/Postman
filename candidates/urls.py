from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.candidates, name='candidates'),  # Список кандидатов
    path('detail/<int:pk>/', views.candidate_detail, name='candidate_detail'),  # детали по конкретному кандидату
    path('create/', views.candidate_create, name='candidate_create'), # создание карточки кандидата
    path('list/upload/', views.candidates_upload, name='candidates_upload'), # загрузка списка кандидатов
    path('edit/<int:pk>/', views.candidate_edit, name='candidate_edit'),  # редактирование карточки кандидата
    path('delete/<int:pk>/', views.candidate_delete, name='candidate_delete'),  # удаление кандидата
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # обработка загружаемых файлов