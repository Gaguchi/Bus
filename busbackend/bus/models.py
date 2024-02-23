from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    trips = models.ManyToManyField('Trip', through='Ticket', related_name='users')

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)

class Transport(models.Model):
    type = models.CharField(max_length=255)
    seats = models.IntegerField()
    rows = models.IntegerField()

class Company(models.Model):
    name = models.CharField(max_length=255)
    routes = models.ManyToManyField('Route', related_name='companies', blank=True)
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True)
    trips = models.ManyToManyField('Trip', related_name='companies', blank=True)

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Route(models.Model):
    cities = models.ManyToManyField(City, through='RouteStop', related_name='routes')

    def __str__(self):
        cities = self.cities.order_by('routestop__order')
        if cities:
            return f"{cities.first()} to {cities.last()} - {self.id}"
        return str(self.id)

    class Meta:
        ordering = ['id']

class RouteStop(models.Model):
    STOP_STATUS_CHOICES = [
        ('U', 'Universal'),
        ('D', 'Departure'),
        ('A', 'Arrival'),
    ]
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    order = models.IntegerField()
    status = models.CharField(max_length=1, choices=STOP_STATUS_CHOICES, default='U')

    class Meta:
        ordering = ['order']

class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='trips')
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='trips')
    time = models.DateTimeField(default=timezone.now)