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
        IOType.UNTYPED: "images/others/connection.png",
        IOType.WATER_INPUT: "images/others/connection.png",
        IOType.WATER_OUTPUT: "images/others/connection.png",
        IOType.DOMESTIC_INPUT: "images/others/connection.png",
        IOType.DOMESTIC_OUTPUT: "images/others/connection.png"
    }
