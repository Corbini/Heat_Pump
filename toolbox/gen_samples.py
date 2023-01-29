from ioobjects import *
from ioobjects.bases import *
from objects.object import Object
from file import save_obj
from pathlib import Path


class GenObj:

    def __init__(self, image_path: str):
        self.path = Path(image_path)
        self.obj = Object(None, None, None, str(self.path))

    def gen_def(self, x, y, iotype: IOType, pointed: Pointed):
        con = IODefined(self.obj, x, y, iotype, pointed)

    def gen_undef(self, x, y, pointed: Pointed):
        con = IOUndefined(self.obj, x, y, pointed)

    def save(self):

        # link all undef connection
        first_undef = None
        for child in self.obj.childItems():
            if isinstance(child, IOUndefined):
                if first_undef is None:
                    first_undef = child
                else:
                    first_undef.link(child)

        path = Path(self.path.stem + ".io")

        save_obj(self.obj, str(path))


def gen_obj():

    gree = GenObj("images/heat_pumps/Gree_Split.png")
    gree.gen_def(512, 381, IOType.WATER_INPUT, Pointed.TOP)
    gree.gen_def(540, 381, IOType.WATER_INPUT, Pointed.TOP)
    gree.gen_def(566, 381, IOType.WATER_OUTPUT, Pointed.BOTTOM)
    gree.save()

    kaisai = GenObj("images/heat_pumps/Kaisai_Split.png")
    kaisai.gen_def(540, 381, IOType.WATER_INPUT, Pointed.TOP)
    kaisai.gen_def(566, 381, IOType.WATER_OUTPUT, Pointed.BOTTOM)
    kaisai.save()

    panasonic = GenObj("images/heat_pumps/Panasonic_Split.png")
    panasonic.gen_def(540, 381, IOType.WATER_INPUT, Pointed.TOP)
    panasonic.gen_def(566, 381, IOType.WATER_OUTPUT, Pointed.BOTTOM)
    panasonic.save()

    radiator = GenObj("images/heat_exchangers/radiators.png")
    radiator.gen_def(0, 3, IOType.WATER_INPUT, Pointed.RIGHT)
    radiator.gen_def(0, 58, IOType.WATER_OUTPUT, Pointed.LEFT)
    radiator.save()

    galmet_1 = GenObj("images/domestic_tanks/Galmet_1_exchanger.png")
    galmet_1.gen_def(15, 137, IOType.WATER_INPUT, Pointed.RIGHT)
    galmet_1.gen_def(15, 223, IOType.WATER_OUTPUT, Pointed.LEFT)
    galmet_1.gen_def(130, 245, IOType.DOMESTIC_INPUT, Pointed.LEFT)
    galmet_1.gen_def(130, 20, IOType.DOMESTIC_OUTPUT, Pointed.RIGHT)
    galmet_1.save()

    pump = GenObj("images/pumps/pump.png")
    pump.gen_undef(-15, 15, Pointed.RIGHT)
    pump.gen_undef(40, 15, Pointed.RIGHT)
    pump.save()
