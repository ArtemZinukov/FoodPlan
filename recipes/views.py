from django.shortcuts import render
from recipes.models import Recipes, Ingredient, RecipeIngredient


def index(request):
    return render(request, 'index.html')


def auth(request):
    return render(request, 'auth.html')


def lk(request):
    return render(request, 'lk.html')


def registration(request):
    return render(request, 'registration.html')


def order(request):
    return render(request, 'order.html')


def card1(request):
    return render(request, 'card1.html')


def card2(request):
    return render(request, 'card2.html')


def card3(request):
    recipe = Recipes.objects.calculate_calories().get(id=1)
    recipe_ingredients = list(RecipeIngredient.objects.filter(recipe=recipe))
    return render(request, 'card3.html', context={'recipe_ingredients': recipe_ingredients,
                  'recipe': recipe}
                  )


