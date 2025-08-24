from django import forms
from candidates.models import Candidate
from data.models import Template
from .models import Vacancy


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

