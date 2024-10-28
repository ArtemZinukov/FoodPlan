from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/auth.html'
    extra_context = {'title': "Авторизация"}

    # def get_success_url(self):
    #     return reverse_lazy('index')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:auth')
