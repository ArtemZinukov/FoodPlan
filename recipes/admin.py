from django.contrib import admin
from .models import Recipes, Ingredient, User, Tariff, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_ingredients')
    search_fields = ('title',)
    list_filter = ('ingredients',)
    fields = ('title', 'description')
    inlines = [
        RecipeIngredientInline
    ]

    def get_ingredients(self, obj):
        return ", ".join([ingredient.title for ingredient in obj.ingredients.all()])
    get_ingredients.short_description = 'Ингредиенты'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories')
    search_fields = ('title',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'tariff')
    search_fields = ('name',)
    list_filter = ('tariff',)


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('time_limit', 'price', 'get_allergies')
    search_fields = ('time_limit',)
    list_filter = ('allergies',)

    def get_allergies(self, obj):
        return obj.allergies
    get_allergies.short_description = 'Аллергии'
