from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Candidate, Vacancy, Template


# Форма регистрации пользователя
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


# Форма входа (логина)
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


# Форма кандидата (заполнение профиля)
class CandidateForm(forms.ModelForm):
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
    )

    class Meta:
        model = Candidate
        fields = ['firstname', 'surname', 'patronymic', 'birthday', 'email', 'phone', 'cv',
                  'vacancies', 'status', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
            'vacancies': forms.CheckboxSelectMultiple(),
        }


# Форма создания вакансии
class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'candidates', 'templates']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'candidates': forms.CheckboxSelectMultiple(),
            'templates': forms.CheckboxSelectMultiple(),
        }


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['title', 'content', 'vacancies']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
            'vacancies': forms.CheckboxSelectMultiple(),
        }