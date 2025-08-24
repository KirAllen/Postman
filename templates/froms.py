from django import forms
from vacancies.models import Vacancy
from .models import Template

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
