from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from .models import *


def home_view(request):
    title = 'Главная страница'
    name_home = 'Главная'
    name_store = 'Магазин'
    name_cart = 'Корзина'
    context = {
        'title': title,
        'name_home': name_home,
        'name_store': name_store,
        'name_cart': name_cart,
    }
    return render(request, 'home.html', context)


def games_view(request):
    title = 'Игры'
    name_home = 'Главная'
    name_store = 'Магазин'
    name_cart = 'Корзина'
    games = Game.objects.all()
    button_buy_title = 'Купить'
    context = {
        'title': title,
        'name_home': name_home,
        'name_store': name_store,
        'name_cart': name_cart,
        'games': games,
        'button_buy_title': button_buy_title,
    }
    return render(request, 'games.html', context)


def cart_view(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    name_home = 'Главная'
    name_store = 'Магазин'
    name_cart = 'Корзина'
    context = {
        'title': title,
        'name_home': name_home,
        'name_store': name_store,
        'name_cart': name_cart,
        'text': text,
    }
    return render(request, 'cart.html', context)


def sign_up(request):
    users = Buyer.objects.values_list('name')
    users = [user[0] for user in users]
    info = dict()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        info['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print(f'username {username}')
            print(f'password {password}')
            print(f'repeat_password {repeat_password}')
            print(f'age {age}')
            if password == repeat_password and age >= 18 and username not in users:
                Buyer.objects.create(name=username, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
    else:
        form = ContactForm()
        info['form'] = form
    return render(request, 'registration_page.html', info)

