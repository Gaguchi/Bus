# Generated by Django 5.0.2 on 2024-06-01 19:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='days_of_week',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='interval',
        ),
        migrations.AddField(
            model_name='trip',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='trip',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]