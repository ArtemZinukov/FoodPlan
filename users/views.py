from django.shortcuts import render


def login_user(request):
    return render(request, 'auth.html')


def logout_user(request):
    return render(request, 'index.html')
