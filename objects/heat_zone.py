# class for heat zone elements
from objects.connections.io_defined import IODefined
from objects.connections.io_types import IOTypes
from enum import Enum


class ZoneTypes(Enum):
    Radiators = 1
    FloorHeater = 2


class HeatZone:
    def __init__(self, zone_type):
        self.ports = []
        self.ports.append(IODefined(IOTypes.WATER_INPUT))
        self.ports.append(IODefined(IOTypes.WATER_OUTPUT))
        self.type = zone_type

    def show(self):
        print("test")
