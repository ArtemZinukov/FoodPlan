from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from users.forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/auth.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('index')



def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'users/registration.html', {'form': form})
    else:
        form = RegisterUserForm()
        return render(request, 'users/registration.html', {'form': form})
