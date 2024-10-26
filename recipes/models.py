from django.db import models
from django.db.models import Sum, F
from tinymce.models import HTMLField


class RecipeQuerySet(models.QuerySet):
    def calculate_calories(self):
        return self.annotate(calories=(Sum(F('recipeingredient__ingredient__calories') * F('recipeingredient__amount')) / 100))


class Recipes(models.Model):
    PUBLICATION_CHOICES = (
            ('Published', 'Опубликовано'),
            ('archived', 'В архиве'),
        )
    title = models.CharField(max_length=200, verbose_name='Название рецепта')
    description = HTMLField(blank=True, verbose_name="Описание рецепта")
    ingredients = models.ManyToManyField('Ingredient', verbose_name="Ингредиенты")
    image = models.ImageField(upload_to='recipes/img', verbose_name="Картинка с рецептом")
    publication = models.CharField(max_length=20, choices=PUBLICATION_CHOICES, default='archived', verbose_name="Опубликовано")

    objects = RecipeQuerySet.as_manager()

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название ингредиента')
    calories = models.PositiveIntegerField(blank=True, null=True, verbose_name="Калории")

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, blank=True, null=True)


    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return f"{self.recipe.title} - {self.ingredient.title}"


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя клиента')
    tariff = models.ForeignKey('Tariff', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тариф")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name


class Tariff(models.Model):
    # TIME_LIMIT_CHOICES = (
    #     ('1_month', '1 месяц'),
    #     ('2_months', '2 месяца'),
    #     ('6_months', 'Полгода'),
    #     ('1_year', '1 год'),
    # )
    # ALLERGY_CHOICES = (
    #     ('none', 'Нет аллергий'),
    #     ('seafood', 'Рыба и морепродукты'),
    #     ('meat', 'Мясо'),
    #     ('grains', 'Зерновые'),
    #     ('honey', 'Продукты пчеловодства'),
    #     ('nuts', 'Орехи и бобовые'),
    #     ('dairy', 'Молочные продукты'),
    # )
    time_limit = models.CharField(max_length=20, verbose_name='Временной лимит')
    # breakfast = models.BooleanField(default=False, verbose_name="Есть завтрак?")
    # dinner = models.BooleanField(default=False, verbose_name="Есть обед?")
    # supper = models.BooleanField(default=False, verbose_name="Есть ужин?")
    # dessert = models.BooleanField(default=False, verbose_name="Есть десерт?")
    # allergies = models.TextField(max_length=20, choices=ALLERGY_CHOICES, default='none', verbose_name="Аллергии")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

    def __str__(self):
        return f"{self.price} - {self.time_limit}"
