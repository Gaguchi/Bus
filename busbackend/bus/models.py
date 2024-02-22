from django.db import models

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

class Company(models.Model):
    name = models.CharField(max_length=255)
    routes = models.ManyToManyField('Route', related_name='companies')
    trips = models.ManyToManyField('Trip', related_name='companies')

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Route(models.Model):
    departures = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_routes')
    arrivals = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_routes')

class Transport(models.Model):
    type = models.CharField(max_length=255)
    seats = models.IntegerField()

class Trip(models.Model):
    departure = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='departure_trips')
    arrival = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='arrival_trips')
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='trips')