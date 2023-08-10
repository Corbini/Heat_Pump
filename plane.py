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


class DrawBoard_Interface(QGraphicsView):
    def __init__(self, window, scene):
        self.plane = QGraphicsScene(0, 0, 1000, 1000)
        super().__init__(self.plane, window)
        self.setAcceptDrops(True)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

        self.scene = scene

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

            obj = load_obj(file_name)

            # getting position (from left top window)
            pos_from = event.position()

            # changing position to view position (from left top view
            pos = self.window().mapFromGlobal(pos_from)

            # changing position to scene position
            x = int(pos.x())
            y = int(pos.y())
            pos_scene = self.mapToScene(x, y)

            # hotspot
            # print(event.)

            # applying pos to object
            # print(pos_from, pos, pos_scene)
            object_id = self.scene.add(obj)
            if object_id == -1:
                print("Error at loading ")
                return

            obj.add_on_scene(pos_scene.x(), pos_scene.y(), object_id, self.plane)

        else:
            print("Incorrent file:", x[1])
        event.acceptProposedAction()


# ProjectBoard
class DrawBoard:

    def __init__(self):
        self.__dictionary = {'': {}}

        gen_obj()

    def new(self):
        del self.__dictionary
        self.__dictionary = {'': {}}

    def __getstate__(self):
        items = map(pickle.dumps, self.__dictionary)

        return "brd", items

    def __setstate__(self, state):
        self.__init__()
        print("reading")
        if state[0] == "brd":
            DrawBoard()

            for item in state[1]:
                constructed_item = pickle.loads(item)
                self.__dictionary[constructed_item.id()] = constructed_item

    def __del__(self):
        del self.__dictionary

    def add(self, item):
        # find empty slot
        for identity_number in range(10000):
            print(self.__dictionary.get(identity_number))
            if self.__dictionary.get(identity_number) is None:
                self.__dictionary[identity_number] = item
                return identity_number

        return -1

    def __add_at(self, item, identity_number):
        # check input
        if identity_number <0 or identity_number >= 10000:
            return -1

        # check if dictonary at id is empty
        if self.__dictionary[identity_number] is not None:
            return -1

        self.__dictionary[identity_number] = item
        return identity_number

    def delete(self):
        pass
