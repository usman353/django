# Generated by Django 2.0.2 on 2018-02-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_auto_20180214_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
