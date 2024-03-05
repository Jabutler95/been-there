# Generated by Django 4.2.10 on 2024-03-05 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_visit_remove_destination_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='visit',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.destination'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(verbose_name='Visit Date'),
        ),
    ]
