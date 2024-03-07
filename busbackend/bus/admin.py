from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from .models import (
    Booking,
    City,
    Company,
    Route,
    RouteStop,
    TransportVehicle,
    Trip,
    User,
    DayOfWeek,
)


class RouteStopInline(SortableInlineAdminMixin, admin.TabularInline):
    model = RouteStop
    extra = 1
    ordering = ['order']


@admin.register(Route)
class RouteAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [RouteStopInline]
    ordering = ['id']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['seat_number', 'passenger', 'trip']
    list_filter = ['trip']
    search_fields = ['seat_number', 'passenger__first_name', 'passenger__last_name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['transport_vehicles', 'trips']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name', 'country']


@admin.register(TransportVehicle)
class TransportVehicleAdmin(admin.ModelAdmin):
    list_display = ['type', 'num_rows', 'num_columns']


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['route', 'transport_vehicle', 'time', 'interval']
    list_filter = ['route', 'transport_vehicle', 'days_of_week']
    filter_horizontal = ['days_of_week']


@admin.register(DayOfWeek)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ['get_day_display']