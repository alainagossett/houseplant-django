# Generated by Django 4.0.2 on 2022-02-24 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watering',
            name='date',
            field=models.DateField(verbose_name='watering date'),
        ),
    ]
