from aria.apps.vehicle.models import Vehicle
from aria.apps.vehicle.serializer import VehicleCreateUpdateSerializer




def create_vehicle(vehicle: Vehicle):
    serializer = VehicleCreateUpdateSerializer(data=vehicle)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False
    