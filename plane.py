from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

# Test
# from objects.connections import *
from objects.object import Object
from objects.heat_source import HeatSource

from ioobjects.bases import *
from ioobjects import *
import pickle


# class for plane
class Plane(QGraphicsView):

    def __init__(self, window):
        self.plane = QGraphicsScene(0, 0, 1000, 1000)
        super().__init__(self.plane, window)
        self.acceptDrops()
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

    def load(self):
        obj = Object(None, None, None, image=QImage("images/heat_pumps/Gree_Split.png"))

        con1 = IOGraphic(obj, 512, 381, IOType.WATER_INPUT)
        obj.add_connection(con1)

        con2 = IODefined(obj, 540, 381, IOType.WATER_INPUT)
        obj.add_connection(con2)

        con3 = IODefined(obj, 566, 381, IOType.WATER_INPUT)
        obj.add_connection(con3)
        self.plane.addItem(obj)

        con4 = IOUndefined(None, 300, 300)
        self.plane.addItem(con4)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.accept()

    def dropEvent(self, event: QDropEvent):
        print("accepted")

