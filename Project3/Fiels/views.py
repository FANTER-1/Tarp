from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Ad
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, CreateAdForm, EditAdForm


def filter_responses(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    responses = ad.responses.all()
    # Реализация фильтрации и действий с откликами
    return render(request, 'responses.html', {'responses': responses})

@login_required
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Обработка формы регистрации
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

@login_required
def create_ad(request):
    if request.method == 'POST':
        form = CreateAdForm(request.POST)
        if form.is_valid():
            # Обработка формы создания объявления
            return redirect('home')  # Перенаправление на главную страницу после создания объявления
    else:
        form = CreateAdForm()
    return render(request, 'create_ad.html', {'form': form})

@login_required
def edit_ad(request, ad_id):
    if request.method == 'POST':
        form = EditAdForm(request.POST)
        if form.is_valid():
            # Обработка формы редактирования объявления
            return redirect('home')  # Перенаправление на главную страницу после редактирования объявления
    else:
        # Загрузка данных объявления для предварительного заполнения формы
        ad = get_object_or_404(Ad, pk=ad_id)
        form = EditAdForm(initial={'title': ad.title, 'description': ad.description, 'price': ad.price})
    return render(request, 'edit_ad.html', {'form': form})

@login_required
def responses(request):
    # Логика обработки откликов на объявления
    return render(request, 'responses.html')

@login_required
def profile(request):
    # Логика отображения приватной страницы пользователя
    return render(request, 'profile.html')


send_mail('Subject', 'Message', 'nazarenko.vitaliy111cool@mail.ru', ['nazarenko.vitaliy111cool@mail.ru'])

send_mail('News', 'Here is the news.', 'nazarenko.vitaliy111cool@mail.ru', ['nazarenko.vitaliy111cool@mail.ru'])



