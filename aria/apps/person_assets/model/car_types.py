from enum import Enum


class CarTypes(Enum):
    # car types enum
    SEDAN = 1
    COUPE = 2
    SPORTS_CAR = 3
    STATION_WAGON = 4
    HATCHBACK = 5
    CONVERTIBLE = 6
    SUV = 7
    MINIVAN = 8
    PICKUP_TRUCK = 9

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
