# class for heat zone elements
from objects.connections.io_defined import IODefined
from objects.connections.io_types import IOTypes
from objects.connections.io_undefined import IOUndefined


class HeatPump:
    def __init__(self):
        self.ports = []
        self.ports.append(IODefined(IOTypes.WATER_INPUT))
        self.ports.append(IODefined(IOTypes.WATER_OUTPUT))

    def show(self):
        print("test")
