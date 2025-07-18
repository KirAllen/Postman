from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Candidate(models.Model):
    # Статусы кандидата
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('interview', 'Назначено собеседование'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонен'),
    ]

    firstname = models.CharField(max_length=100, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=100, verbose_name='Фамилия', blank=True)
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True)
    email = models.EmailField(verbose_name='E-mail', blank=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True)
    cv = models.FileField(
        upload_to='cvs/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        blank=True,
        null=True,
        verbose_name='Резюме'
    )
    vacancies = models.ManyToManyField('Vacancy', blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'

    def __str__(self):
        return f'Кандидат: {self.firstname} {self.surname} {self.patronymic}'


class Template(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    vacancies = models.ManyToManyField('Vacancy', blank=True)

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"

    def __str__(self):
        return f'Письмо: {self.title}'


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vacancies",
        verbose_name="Пользователь"
    )
    candidates = models.ManyToManyField(Candidate, blank=True)
    templates = models.ManyToManyField(Template, blank=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f'Вакансия: {self.title}'
