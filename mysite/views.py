from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {"header": "Homepage", "message": "Добро пожаловать на мой сайт! Здесь будут статьи на разные, интересные мне темы. Перейте к ним можете через хэдер."}
    return render(request, 'homepage.html', context=data)

def about(request):
    header = "About us"
    staff = ['Nicola Tesla', 'Tim Berners Lee', 'Guido van Rossum']
    director = {"name": "David Lee", "img": '/director.jpg'}
    address = ('20 W 34tg St.', 'New York', 'NY 10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)