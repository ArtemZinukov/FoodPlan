from django.http import HttpResponse


def auth_user(request):
    return HttpResponse("<h1>Welcome to Django</h1>")


def registration_user(request):
    return HttpResponse("<h1>Registration DONE!!!</h1>")
