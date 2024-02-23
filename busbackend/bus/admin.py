from django.contrib import admin
from .models import User, Ticket, Company, City, Route, RouteStop, Transport, Trip
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin

class RouteStopInline(SortableInlineAdminMixin, admin.TabularInline):
    model = RouteStop
    extra = 1
    ordering = ['order']

class RouteAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [RouteStopInline]
    ordering = ['id']

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Company)
admin.site.register(City)
admin.site.register(Route, RouteAdmin)
admin.site.register(Transport)
admin.site.register(Trip)