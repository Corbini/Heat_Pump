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


#
# class Restriction:
#
#     def check():
#         return None
#
# class Item:
#     def __init__(self, image, position_x: int, position_y: int,  restrictions = list(), connector_change = False):
#         self.graphic_interface = QGraphicsPixmapItem()
#         self.graphic_interface.setPixmap(image)
#         self.graphic_interface.setX(position_x)
#         self.graphic_interface.setY(position_y)
#
#         self.__connection_change = connector_change
#         self.__connectors = dict()
#         self.__connectors_count = 0
#         self.__restrictions = restrictions
#         self.__identity_number = DRAWBOARD.add(self)
#
#
#     def add_connection(self, type: IOType):
#         self.__connectors[self.__connectors_count] = Connector(type)
#
#     def __change_connectors_type(self):
#         if self.__connection_change is False:
#             return
#
#         for connector in self.__connectors:
#             if connector.is_linked():
#                 return
#
#         for connector in self.__connectors:
#             connector.type = IOType.UNTYPED
#
#     def check_restrictions(self):
#         not_passed = list()
#         for restriction in self.__restrictions:
#             status = restriction()
#             if status is not None:
#                not_passed.append(status)
#
#     def get_identity(self):
#         return int(self.__identity_number)
#


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

            # hotspot
            # print(event.)

            # applying pos to object
            # print(pos_from, pos, pos_scene)
            obj.setPos(pos_scene.x(), pos_scene.y())
            status = self.scene.add(obj)
            if status == -1:
                print("Error at loading ")

            self.plane.addItem(obj)
        else:
            print("Incorrent file:", x[1])
        event.acceptProposedAction()


# ProjectBoard
class DrawBoard:

    def __init__(self, window):
        self.__dictionary = {'': {}}

        gen_obj()

    def new(self):
        del self.__dictionary
        self.__dictionary = {'': {}}

    def load(self, file_path: str):
        pass

    def __del__(self):
        del self.__dictionary

    def add(self, item):
        # find empty slot
        for identity_number in range(10000):
            print(self.__dictionary.get(identity_number))
            if self.__dictionary.get(identity_number) is None:
                self.__dictionary[identity_number] = Item

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
