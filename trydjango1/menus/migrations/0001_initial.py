# Generated by Django 2.0.2 on 2018-02-18 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0014_restaurantlocation_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('contents', models.TextField(blank=True, help_text='separate_by_commas', null=True)),
                ('public', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.RestaurantLocation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]
