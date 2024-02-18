from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, related_name='tickets')

class Company(models.Model):
    name = models.CharField(max_length=255)
    transport = models.CharField(max_length=255)

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Route(models.Model):
    departures = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_routes')
    arrivals = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_routes')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='routes')

class Trip(models.Model):
    departure = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='departure_trips')
    arrival = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='arrival_trips')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='trips')

class UserTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

class CompanyTrip(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)