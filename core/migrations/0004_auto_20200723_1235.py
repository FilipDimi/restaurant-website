# Generated by Django 3.0.7 on 2020-07-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200723_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='second_price',
            field=models.FloatField(blank=True),
        ),
    ]
