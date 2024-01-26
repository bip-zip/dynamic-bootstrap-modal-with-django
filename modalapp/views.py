from django.views.generic import ListView
from .models import ParkingLot, Vehicle
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET

class HomeView(ListView):
    template_name = 'home.html'
    model = ParkingLot
    context_object_name = 'objects'



@require_GET
def get_modal_content(request):
    modal_id = request.GET.get('id')
    parking_lot_instance = get_object_or_404(ParkingLot, id=modal_id)

    modal_data = {
        'name':parking_lot_instance.name,
        'vehicles': [
            {'vehicle': vehicle.vehicle_type,'vehicle_no': vehicle.vehicle_number, 'entry_time':vehicle.entry_time }
            for vehicle in parking_lot_instance.vehicles.all()
        ],
    }
    print(modal_data)
    return JsonResponse(modal_data)

