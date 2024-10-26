from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('auth/', views.login_user, name='auth'),
    path('logout/', views.logout_user, name='logout')
]
