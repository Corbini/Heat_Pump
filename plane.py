from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

# Test
from objects.connections import *
from objects.object import AbstractObject


# class for plane
class Plane(QGraphicsView):

    def __init__(self, window):
        self.plane = QGraphicsScene(0, 0, 1000, 1000)
        super().__init__(self.plane, window)

    def load(self):
        obj = Object(None, None, None, image=QImage("images/heat_pumps/Gree_Split.png"))

        con1 = IODefined(IOTypes.WATER_INPUT, 512, 381)
        obj.add_connection(con1)

        con2 = IODefined(IOTypes.WATER_INPUT, 540, 381)
        obj.add_connection(con2)

        con3 = IODefined(IOTypes.WATER_INPUT, 566, 381)
        obj.add_connection(con3)
        self.plane.addItem(obj)

        obj2 = Object(obj, 200, 200)
        self.plane.addItem(obj2)

        obj.setPos(200, 200)


