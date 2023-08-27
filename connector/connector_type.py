from enum import Enum


class Pointed(Enum):
    TOP = 0
    RIGHT = 90
    BOTTOM = 180
    LEFT = 270


class ConnectorType(Enum):
    UNTYPED = 0
    WATER_INPUT = 1
    WATER_OUTPUT = 2
    DOMESTIC_INPUT = 4
    DOMESTIC_OUTPUT = 5

    def path(self) -> str:
        return path_list[self]


path_list = {
        ConnectorType.UNTYPED: "images/connections/untyped.png",
        ConnectorType.WATER_INPUT: "images/connections/water_input.png",
        ConnectorType.WATER_OUTPUT: "images/connections/water_output.png",
        ConnectorType.DOMESTIC_INPUT: "images/connections/domestic_input.png",
        ConnectorType.DOMESTIC_OUTPUT: "images/connections/domestic_output.png"
    }

