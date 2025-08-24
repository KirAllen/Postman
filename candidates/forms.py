from django import forms

from .models import Candidate
from data.models import Vacancy


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


# Форма для загрузки файла данными кандидата
class UploadCandidatesForm(forms.Form):
    file = forms.FileField(label="Файл Excel (.xlsx)")
