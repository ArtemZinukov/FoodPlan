from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Имя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    verif_password = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        labels = {
            'username': 'Имя',
            'email': 'E-mail',
            'password': 'Пароль'
        }

    def clean_verif_password(self):
        password = self.cleaned_data.get('password')
        verif_password = self.cleaned_data.get('verif_password')
        if password and verif_password and password != verif_password:
            raise ValidationError('Пароли не совпадают')
        return verif_password

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой E-mail уже существует')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        if commit:
            user.save()
        return user

