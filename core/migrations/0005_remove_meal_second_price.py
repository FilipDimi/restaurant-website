# Generated by Django 3.0.7 on 2020-07-23 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200723_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='second_price',
        ),
    ]