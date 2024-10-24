# Generated by Django 4.2.8 on 2024-10-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='time_limit',
            field=models.CharField(choices=[('1_month', '1 месяц'), ('2_months', '2 месяца'), ('6_months', 'Полгода'), ('1_year', '1 год')], default='1_month', max_length=20, verbose_name='Временной лимит'),
        ),
    ]