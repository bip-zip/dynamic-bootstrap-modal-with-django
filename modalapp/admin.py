from django.contrib import admin
from .models import ParkingLot, Vehicle

class VehicleInline(admin.TabularInline):
    model = Vehicle
    extra = 0

class ParkingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vehicle_capacity' )
    inlines = [VehicleInline]

admin.site.register(ParkingLot, ParkingAdmin)
