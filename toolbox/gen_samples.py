from connector import *
from object.object import Object


def gen_obj():

    gree = Object("images/heat_pumps/Gree_Split.png")
    gree.add_connector(512, 381, ConnectorType.WATER_INPUT, Pointed.TOP)
    gree.add_connector(540, 381, ConnectorType.WATER_INPUT, Pointed.TOP)
    gree.add_connector(566, 381, ConnectorType.WATER_OUTPUT, Pointed.BOTTOM)
    gree.sample()

    kaisai = Object("images/heat_pumps/Kaisai_Split.png")
    kaisai.add_connector(540, 381, ConnectorType.WATER_INPUT, Pointed.TOP)
    kaisai.add_connector(566, 381, ConnectorType.WATER_OUTPUT, Pointed.BOTTOM)
    kaisai.sample()

    panasonic = Object("images/heat_pumps/Panasonic_Split.png")
    panasonic.add_connector(540, 381, ConnectorType.WATER_INPUT, Pointed.TOP)
    panasonic.add_connector(566, 381, ConnectorType.WATER_OUTPUT, Pointed.BOTTOM)
    panasonic.sample()

    radiator = Object("images/heat_exchangers/radiators.png")
    radiator.add_connector(0, 3, ConnectorType.WATER_INPUT, Pointed.RIGHT)
    radiator.add_connector(0, 58, ConnectorType.WATER_OUTPUT, Pointed.LEFT)
    radiator.sample()

    galmet_1 = Object("images/domestic_tanks/Galmet_1_exchanger.png")
    galmet_1.add_connector(15, 137, ConnectorType.WATER_INPUT, Pointed.RIGHT)
    galmet_1.add_connector(15, 223, ConnectorType.WATER_OUTPUT, Pointed.LEFT)
    galmet_1.add_connector(130, 245, ConnectorType.DOMESTIC_INPUT, Pointed.LEFT)
    galmet_1.add_connector(130, 20, ConnectorType.DOMESTIC_OUTPUT, Pointed.RIGHT)
    galmet_1.sample()

    pump = Object("images/pumps/pump.png")
    pump.add_connector(-15, 15, ConnectorType.UNTYPED, Pointed.RIGHT)
    pump.add_connector(40, 15, ConnectorType.UNTYPED, Pointed.RIGHT)
    pump.sample()
