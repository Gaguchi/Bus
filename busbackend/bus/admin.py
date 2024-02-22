from django.contrib import admin
from .models import User, Ticket, Company, City, Route, Transport, Trip

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Company)
admin.site.register(City)
admin.site.register(Route)
admin.site.register(Transport)
admin.site.register(Trip)