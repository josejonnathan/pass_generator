from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, "home.html")


def password(request):
    char_list = list('abcdefghijklmnopqrstuvxyz')
    generated_password = ''
    lenght = int(request.GET.get('length'))
    upper = request.GET.get('uppercase')
    special = request.GET.get('special')
    numbers = request.GET.get('numbers')

    if upper:
        char_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if special:
        char_list.extend(list('_-?[]?$%&#@'))

    if numbers:
        char_list.extend(list('123456789'))

    for x in range(lenght):
        generated_password += random.choice(char_list)

    return render(request, 'home.html', {'password': generated_password})
