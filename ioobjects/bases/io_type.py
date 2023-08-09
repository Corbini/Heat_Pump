from enum import Enum


class IOType(Enum):
    UNTYPED = 0
    WATER_INPUT = 1
    WATER_OUTPUT = 2
    DOMESTIC_INPUT = 4
    DOMESTIC_OUTPUT = 5

    def path(self) -> str:
        return path_list[self]


path_list = {
        IOType.UNTYPED: "images/connections/untyped.png",
        IOType.WATER_INPUT: "images/connections/water_input.png",
        IOType.WATER_OUTPUT: "images/connections/water_output.png",
        IOType.DOMESTIC_INPUT: "images/connections/domestic_input.png",
        IOType.DOMESTIC_OUTPUT: "images/connections/domestic_output.png"
    }

