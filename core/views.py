from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html', {})


def login(request):
    return render(request, 'home/login.html', {})


def criarConta(request):
    return render(request, 'home/createCount.html', {})