from .models import Vacancy, Candidate, Template
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, VacancyForm, TemplateForm, CandidateForm, UploadCandidatesForm

import openpyxl

from .emails import send_email_to_candidate

@login_required
def dashboard(request):
    return render(request, 'data/dashboard.html')

# шаблоны писем кандидатам
@login_required
def templates(request):
    templates = Template.objects.all()
    return render(request, 'data/templates.html', {'templates': templates})

# список всех кандидатов
@login_required
def candidates(request):
    candidates = Candidate.objects.all()
    return render(request, 'data/candidates.html', {'candidates' : candidates})

# подробная информация о кандидате
@login_required
def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'data/candidate_detail.html', {'candidate': candidate})

@login_required
def candidate_create(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()
            # Обновим связанные вакансии вручную
            candidate.vacancies.clear()  # Убираем все старые связи
            for vacancy in form.cleaned_data['vacancies']:
                vacancy.candidates.add(candidate)
            return redirect('candidates')
    else:
        form = CandidateForm()
    return render(request, 'data/candidate_create.html', {'form': form})

# редактирование карточки кандидата
@login_required
def candidate_edit(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            candidate = form.save()
            # Обновим связанные вакансии вручную
            candidate.vacancies.clear()  # Убираем все старые связи
            for vacancy in form.cleaned_data['vacancies']:
                vacancy.candidates.add(candidate)
            return redirect('candidate_detail', pk=candidate.pk)
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'data/candidate_create.html', {'form': form, 'editing': True})

@login_required
def candidates_upload(request):
    if request.method == 'POST':
        form = UploadCandidatesForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                firstname, surname, patronymic, birthday, email, phone = row[:6]

                # Не создавать, если пустой email
                if not email:
                    continue

                Candidate.objects.create(
                    firstname=firstname,
                    surname=surname,
                    patronymic=patronymic,
                    birthday=birthday,
                    email=email,
                    phone=phone
                )

            return redirect('candidates')
    else:
        form = UploadCandidatesForm()
    return render(request, 'data/candidates_upload.html', {'form': form})


@login_required
def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        candidate.delete()
        return redirect('candidates')
    return render(request, 'data/candidate_detail.html', {'candidate': candidate})


# список вакансий
@login_required
def vacancies(request):
    vacancies = Vacancy.objects.filter(user=request.user)
    return render(request, 'data/vacancies.html', {'vacancies': vacancies})


# создание новой вакансии
@login_required
def vacancy_create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.user = request.user
            vacancy.save()
            form.save_m2m()
            return redirect('vacancies')
    else:
        form = VacancyForm()
    return render(request, 'data/vacancy_create.html', {'form': form})


# подробная информация о вакансии
@login_required
def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'data/vacancy_detail.html', {'vacancy': vacancy})

# редактирование вакансии
@login_required
def vacancy_edit(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)

    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.save()
            form.save_m2m()
        return redirect('vacancy_detail', pk=vacancy.pk)
    else:
        form = VacancyForm(instance=vacancy)

    return render(request, 'data/vacancy_create.html', {'form': form, 'editing': True})

# удаление вакансии
@login_required
def vacancy_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        vacancy.delete()
        return redirect('vacancies')
    return render(request, 'data/vacancy_detail.html', {'vacancy': vacancy})

@login_required
def template_create(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
            template = form.save()
            # Обновим связанные вакансии вручную
            template.vacancies.clear()  # Убираем все старые связи
            for vacancy in form.cleaned_data['vacancies']:
                vacancy.templates.add(template)
            return redirect('templates')
    else:
        form = TemplateForm()
    return render(request, 'data/template_create.html', {'form': form})


@login_required
def template_edit(request, pk):
    template = get_object_or_404(Template, pk=pk)

    if request.method == 'POST':
        form = TemplateForm(request.POST, instance=template)
        if form.is_valid():
            template = form.save()
            # Сбрасываем старые связи
            template.vacancies.clear()
            # Устанавливаем новые
            for vacancy in form.cleaned_data['vacancies']:
                vacancy.templates.add(template)
            return redirect('template_detail', pk=template.pk)
    else:
        form = TemplateForm(instance=template)

    return render(request, 'data/template_create.html', {'form': form, 'editing': True})

@login_required
def template_detail(request, pk):
    template = get_object_or_404(Template, pk=pk)
    return render(request, 'data/template_detail.html', {'template': template})

@login_required
def template_delete(request, pk):
    template = get_object_or_404(Template, pk=pk)
    if request.method == 'POST':
        template.delete()
        return redirect('templates')
    return render(request, 'data/template_detail.html', {'template': template})

@login_required
def send_vacancy_emails(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    candidates = vacancy.candidates.all()
    templates = vacancy.templates.all()

    if not templates.exists():
        messages.error(request, "Нет шаблона письма, прикрепленного к вакансии.")
        return redirect('vacancy_detail', pk=vacancy_id)

    # Например, используем первый шаблон
    template = templates.first()

    for candidate in candidates:
        if candidate.email:
            send_email_to_candidate(candidate, template)

    messages.success(request, f"Письма успешно отправлены {candidates.count()} кандидатам.")
    return redirect('vacancy_detail', pk=vacancy_id)


# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'data/register.html', {'form': form})

# Вход пользователя
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'data/login.html', {'form': form})


# Выход пользователя
def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('/data/login')