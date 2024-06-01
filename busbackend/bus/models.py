from django.db import models
from django.utils import timezone
from datetime import timedelta, datetime
from string import ascii_uppercase
from calendar import monthrange

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    trips = models.ManyToManyField('Trip', through='Booking', related_name='passengers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    seat_number = models.CharField(max_length=255)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return f"{self.seat_number} - {self.trip}"

class DayOfWeek(models.Model):
    DAY_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]
    day = models.IntegerField(choices=DAY_CHOICES)

    def __str__(self):
        return self.get_day_display()

class TransportVehicle(models.Model):
    type = models.CharField(max_length=255)
    num_columns = models.PositiveIntegerField()
    num_rows = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} ({self.num_rows} x {self.num_columns})"

class Company(models.Model):
    name = models.CharField(max_length=255)
    transport_vehicles = models.ManyToManyField(TransportVehicle, related_name='companies')
    trips = models.ManyToManyField('Trip', related_name='companies', blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}, {self.country}"

class Route(models.Model):
    cities = models.ManyToManyField(City, through='RouteStop', related_name='routes')

    def __str__(self):
        route_stops = self.stops.order_by('order')
        if route_stops:
            first_city = route_stops.first().city
            last_city = route_stops.last().city
            return f"{first_city} to {last_city} - {self.id}"
        return str(self.id)

    class Meta:
        ordering = ['id']

class RouteStop(models.Model):
    STOP_STATUS_CHOICES = [
        ('U', 'Universal'),
        ('D', 'Departure'),
        ('A', 'Arrival'),
    ]
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='stops')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_stops')
    order = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=STOP_STATUS_CHOICES, default='U')

    class Meta:
        ordering = ['order']
        unique_together = ('route', 'order')

class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='trips')
    transport_vehicle = models.ForeignKey(TransportVehicle, on_delete=models.CASCADE, related_name='trips')
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"{self.route} - {self.date} - {self.time}"