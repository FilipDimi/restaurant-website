# Generated by Django 3.0.7 on 2020-07-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_meal_second_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='second_price',
            field=models.FloatField(default=-1),
        ),
    ]
