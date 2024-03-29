# Generated by Django 5.0.2 on 2024-03-07 13:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TransportVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('num_columns', models.PositiveIntegerField()),
                ('num_rows', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RouteStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('U', 'Universal'), ('D', 'Departure'), ('A', 'Arrival')], default='U', max_length=1)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_stops', to='bus.city')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='bus.route')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('route', 'order')},
            },
        ),
        migrations.AddField(
            model_name='route',
            name='cities',
            field=models.ManyToManyField(related_name='routes', through='bus.RouteStop', to='bus.city'),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.PositiveIntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('days_of_week', models.ManyToManyField(blank=True, to='bus.dayofweek')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='bus.route')),
                ('transport_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='bus.transportvehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('transport_vehicles', models.ManyToManyField(related_name='companies', to='bus.transportvehicle')),
                ('trips', models.ManyToManyField(blank=True, related_name='companies', to='bus.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=255)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='bus.trip')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('trips', models.ManyToManyField(related_name='passengers', through='bus.Booking', to='bus.trip')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='bus.user'),
        ),
    ]
