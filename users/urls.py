from django.contrib.auth.views import LogoutView
from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('auth/', views.LoginUser.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.register, name='registration' ),
]
