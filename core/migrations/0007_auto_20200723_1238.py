# Generated by Django 3.0.7 on 2020-07-23 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_meal_second_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dessert',
        ),
        migrations.DeleteModel(
            name='Soup',
        ),
    ]