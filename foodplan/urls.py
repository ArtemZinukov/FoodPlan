from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from recipes import views
from recipes.models import Recipes, Ingredient, RecipeIngredient


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('auth/', views.auth, name='auth'),
    path('lk/', views.lk, name='lk'),
    path('order/', views.order, name='order'),
    path('registration/', views.registration, name='registration'),
    path('card1/', views.card1, name='card1'),
    path('card2/', views.card2, name='card2'),
    path('card3/', views.card3, name='card3'),
    path('tinymce/', include('tinymce.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)