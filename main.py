from application import Application
from objects.connections.io_undefined import IOUndefined
from objects.connections.io_defined import IODefined
from objects.connections.io_types import IOTypes

def main():
    group = [IOUndefined(), IOUndefined(), IOUndefined()]
    group[0].link(group[1])
    group[0].link(group[2])

    water_intake = IODefined(IOTypes.WATER_INPUT)
    water_intake2 = IODefined(IOTypes.WATER_INPUT)

    water_output = IODefined(IOTypes.WATER_OUTPUT)

    water_intake.connect(group[0])
    water_intake.disconnect()
    water_intake.connect(group[0])
    water_intake2.connect(group[1])
    water_intake.disconnect()
    water_output.connect(group[2])

    # Application()


main()
