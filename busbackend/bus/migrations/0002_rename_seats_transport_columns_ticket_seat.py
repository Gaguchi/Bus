# Generated by Django 5.0.2 on 2024-02-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transport',
            old_name='seats',
            new_name='columns',
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]