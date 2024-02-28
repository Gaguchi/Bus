from django.db import models
from django.utils import timezone
from string import ascii_uppercase

class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    trips = models.ManyToManyField('Trip', through='Ticket', related_name='users')

    def __str__(self):
        return str(self.name)

class Ticket(models.Model):
    seat = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.seat} - {self.trip}"

class Transport(models.Model):
    type = models.CharField(max_length=255)
    columns = models.IntegerField()
    rows = models.IntegerField()
    
    def __str__(self):
        return f"{self.type} - {self.rows}/{self.columns}"

class Company(models.Model):
    name = models.CharField(max_length=255)
    routes = models.ManyToManyField('Route', related_name='companies', blank=True)
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True)
    trips = models.ManyToManyField('Trip', related_name='companies', blank=True)

    def __str__(self):
        return str(self.name)

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

    def __str__(self):
        return f"{self.route} - {self.time}"

    def save(self, *args, **kwargs):
        is_new = not self.pk  # check if this is a new instance
        super().save(*args, **kwargs)  # call the original save method

        if is_new:  # if this is a new instance
            for row in range(1, self.transport.rows + 1):
                for col in ascii_uppercase[:self.transport.columns]:
                    seat = f"{row}{col}"
                    Ticket.objects.create(seat=seat, trip=self)