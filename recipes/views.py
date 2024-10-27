from django.conf import settings
from django.shortcuts import render, redirect
from recipes.models import Recipes, Ingredient, RecipeIngredient, Tariff
from yookassa import Configuration, Payment

Configuration.configure(settings.YOOKASSA_SHOP_ID,
                        settings.YOOKASSA_SECRET_KEY)


def index(request):
    return render(request, 'index.html')


def lk(request):
    return render(request, 'users/lk.html')


def create_order(request):
    tariffs = Tariff.objects.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            tariff_id = request.POST.get('tariff_id')

            tariff = Tariff.objects.get(id=tariff_id)

            payment = Payment.create({
                "amount": {
                    "value": str(tariff.price),
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": request.build_absolute_uri('/')
                },
                "capture": True,
                "description": f"Заказ на тариф {tariff.time_limit}"
            })

            return redirect(payment.confirmation.confirmation_url)
        else:
            return redirect('users:auth')

    return render(request, 'order.html', {'tariffs': tariffs})


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


