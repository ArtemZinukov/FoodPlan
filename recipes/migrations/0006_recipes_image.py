# Generated by Django 4.2.8 on 2024-10-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipeingredient_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='image',
            field=models.ImageField(default=1, upload_to='recipes/img', verbose_name='Картинка с рецептом'),
            preserve_default=False,
        ),
    ]