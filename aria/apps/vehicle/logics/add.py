from aria.apps.vehicle.models import Vehicle
from aria.apps.vehicle.serializer import VehicleSerializer




def create_vehicle(info: Vehicle):
    serializer = VehicleSerializer(data=info)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return True
    return False
    


def validate_vehicle_data(info:Vehicle):
    vehicleSerializer = VehicleSerializer(data=info)
    if vehicleSerializer.is_valid(raise_exception=True): 
        return True
    return False