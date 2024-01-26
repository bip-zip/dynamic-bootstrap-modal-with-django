from django.db import models

class ParkingLot(models.Model):
    name = models.CharField(max_length = 50, null=False, unique=True)
    vehicle_capacity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name
    
    @property
    def remaining_space(self):
        pass
    
class Vehicle(models.Model):
    VEHICLE_TYPE=(("Bike", "bike"),
                ("Car", "car"),
                ("Scooter", "scooter"),)

    parkinglot= models.ForeignKey(ParkingLot, on_delete =models.CASCADE)
    vehicle_type= models.CharField(max_length = 12, choices = VEHICLE_TYPE, default ='bike')
    vehicle_number = models.CharField(max_length = 50, null=False, blank=False)
    color= models.CharField(max_length = 20, null=False)
    brand = models.CharField(max_length = 30, null= False)
    entry_time = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.vehicle_number