# Generated by Django 4.2.10 on 2024-03-05 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]