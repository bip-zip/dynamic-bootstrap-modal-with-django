from django.views.generic import ListView
from .models import ParkingLot, Vehicle

class HomeView(ListView):
    template_name = 'home.html'
    model = ParkingLot
    context_object_name = 'objects'



