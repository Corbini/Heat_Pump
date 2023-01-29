from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

# Test
from objects.object import Object

from ioobjects.bases import *
from ioobjects import *
import pickle
from file import save_obj, load_obj
from toolbox.gen_samples import gen_obj


# class for plane
class Plane(QGraphicsView):

    def __init__(self, window):
        self.plane = QGraphicsScene(0, 0, 1000, 1000)
        super().__init__(self.plane, window)
        self
        self.setAcceptDrops(True)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

    @staticmethod
    def _loadobj(self, path):
        with open(path, "rb") as handle:
            return pickle.load(handle)

    def load(self):

        # self.test_obj()
        gen_obj()
        pass

    def test_obj(self):
        obj = Object(None, 100, 100, "images/pumps/pump.png")
        obj.setPos(100, 100)
        con = IOUndefined(obj, -15, 15, Pointed.RIGHT)
        con = IOUndefined(obj, 40, 15, Pointed.RIGHT)

        self.plane.addItem(obj)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText:
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        if event.mimeData().hasText:
            # print("accepts drop")
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        print('dropped')
        file_name = event.mimeData().text()
        x = file_name.split('.')
        if x[1] == 'io':
            # obj = load_obj(path)
            obj = load_obj(file_name)

            # getting position (from left top window)
            pos_from = event.position()

            # changing position to view position (from left top view
            pos = self.window().mapFromGlobal(pos_from)

            # changing position to scene position
            x = int(pos.x())
            y = int(pos.y())
            pos_scene = self.mapToScene(x, y)

            #hotspot
            # print(event.)

            # applying pos to object
            # print(pos_from, pos, pos_scene)
            obj.setPos(pos_scene.x(), pos_scene.y())
            self.plane.addItem(obj)
        else:
            print("Incorrent file:", x[1])
        event.acceptProposedAction()



