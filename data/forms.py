from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Candidate, Vacancy, Template

from registration.models import User


# # Форма входа (логина)
# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(label='Имя пользователя', max_length=100)
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


# Форма кандидата (заполнение профиля)
class CandidateForm(forms.ModelForm):
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'], label="Дата рождения"
    )

    vacancies = forms.ModelMultipleChoiceField(
        queryset=Vacancy.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Вакансии"
    )

    class Meta:
        model = Candidate
        fields = [
            'firstname',
            'surname',
            'patronymic',
            'birthday',
            'email',
            'phone',
            'tg',
            'cv',
            'vacancies',
            'status',
            'notes',
            'vacancies',
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        # получаем instance, если он передан
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        if instance:
            # Выставляем начальные значения для поля vacancies
            self.fields['vacancies'].initial = instance.vacancies.all()


# Форма создания вакансии
class VacancyForm(forms.ModelForm):
    candidates = forms.ModelMultipleChoiceField(
        queryset=Candidate.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Кандидаты"
    )

    templates = forms.ModelMultipleChoiceField(
        queryset=Template.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Письма"
    )

    class Meta:
        model = Vacancy
        fields = ['title',
                  'description',
                  'candidates',
                  'templates']


# Форма создания письма
class TemplateForm(forms.ModelForm):
    vacancies = forms.ModelMultipleChoiceField(
        queryset=Vacancy.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Вакансии"
    )

    class Meta:
        model = Template
        fields = ['title', 'content', 'vacancies']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        # получаем instance, если он передан
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        if instance:
            # Выставляем начальные значения для поля vacancies
            self.fields['vacancies'].initial = instance.vacancies.all()


# Форма редактирования профиля пользователя
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


# Форма для загрузки файла данными кандидата
class UploadCandidatesForm(forms.Form):
    file = forms.FileField(label="Файл Excel (.xlsx)")
