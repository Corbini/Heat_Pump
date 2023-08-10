from ioobjects import *
from ioobjects.bases import *
from objects.object import Object
from pathlib import Path



def gen_obj():

    gree = Object("images/heat_pumps/Gree_Split.png")
    gree.add_io_defined(512, 381, IOType.WATER_INPUT, Pointed.TOP)
    gree.add_io_defined(540, 381, IOType.WATER_INPUT, Pointed.TOP)
    gree.add_io_defined(566, 381, IOType.WATER_OUTPUT, Pointed.BOTTOM)
    gree.sample()

    kaisai = Object("images/heat_pumps/Kaisai_Split.png")
    kaisai.add_io_defined(540, 381, IOType.WATER_INPUT, Pointed.TOP)
    kaisai.add_io_defined(566, 381, IOType.WATER_OUTPUT, Pointed.BOTTOM)
    kaisai.sample()

    panasonic = Object("images/heat_pumps/Panasonic_Split.png")
    panasonic.add_io_defined(540, 381, IOType.WATER_INPUT, Pointed.TOP)
    panasonic.add_io_defined(566, 381, IOType.WATER_OUTPUT, Pointed.BOTTOM)
    panasonic.sample()

    radiator = Object("images/heat_exchangers/radiators.png")
    radiator.add_io_defined(0, 3, IOType.WATER_INPUT, Pointed.RIGHT)
    radiator.add_io_defined(0, 58, IOType.WATER_OUTPUT, Pointed.LEFT)
    radiator.sample()

    galmet_1 = Object("images/domestic_tanks/Galmet_1_exchanger.png")
    galmet_1.add_io_defined(15, 137, IOType.WATER_INPUT, Pointed.RIGHT)
    galmet_1.add_io_defined(15, 223, IOType.WATER_OUTPUT, Pointed.LEFT)
    galmet_1.add_io_defined(130, 245, IOType.DOMESTIC_INPUT, Pointed.LEFT)
    galmet_1.add_io_defined(130, 20, IOType.DOMESTIC_OUTPUT, Pointed.RIGHT)
    galmet_1.sample()

    pump = Object("images/pumps/pump.png")
    pump.add_io_undefined(-15, 15, Pointed.RIGHT)
    pump.add_io_undefined(40, 15, Pointed.RIGHT)
    pump.sample()
