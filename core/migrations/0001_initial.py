# Generated by Django 3.0.7 on 2020-06-30 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeverageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.FloatField(blank=True, default=-1.0)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('ingredients', models.ManyToManyField(blank=True, to='core.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_today_special', models.BooleanField(default=False)),
                ('meal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('meal_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MealCategory')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MealCategory'),
        ),
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(blank=True, default=-1)),
                ('beverage_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.BeverageCategory')),
            ],
        ),
    ]
