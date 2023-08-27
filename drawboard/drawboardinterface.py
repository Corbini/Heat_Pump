from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from eventhandler import Caller, Event, AddObj


class DrawBoardInterface(QGraphicsView, Caller):
    def __init__(self):
        self.plane = QGraphicsScene(0, 0, 1000, 1000)
        super().__init__(self.plane)
        self.setAcceptDrops(True)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText:
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        if event.mimeData().hasText:
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        print('dropped')
        file_name = event.mimeData().text()
        x = file_name.split('.')
        if x[1] == 'io':

            # getting position (from left top window)
            pos_from = event.position()

            # changing position to view position (from left top view
            pos = self.window().mapFromGlobal(pos_from)

            # changing position to scene position
            x = int(pos.x())
            y = int(pos.y())
            pos_scene = self.mapToScene(x, y)

            add_obj = AddObj()
            add_obj.file_name = file_name
            add_obj.x = pos_scene.x()
            add_obj.y = pos_scene.y()
            print({file_name}, {add_obj.x}, {add_obj.y})
            self.call(Event.ADD_OBJ, add_obj)

        else:
            print("Incorrent file:", x[1])
        event.acceptProposedAction()

    def set_window(self, window):
        self.setParent(window)

    def set_view_size(self, left: int, top: int, width: int, height: int):
        self.setGeometry(left, top, width, height)

    def add_item(self, item):
        self.plane.addItem(item)
