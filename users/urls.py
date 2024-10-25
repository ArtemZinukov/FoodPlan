from django.urls import path, include

from users import views


app_name = 'users'
urlpatterns = [
    path('auth/', views.auth_user, name='auth'),
    path('registration/', views.registration_user, name='registration'),
]
