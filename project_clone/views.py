from django.shortcuts import render


def home(request):
    return render(request, 'users/home.html')


def about(request):
    return render(request, 'user/about.html')


def chat(request):
    return render(request, 'user/chat.html')
