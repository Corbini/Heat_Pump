import pickle

from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem, QGraphicsScene
from PyQt6.QtGui import QPixmap, QImage
from ioobjects.bases import *
from ioobjects import *


class Object(QGraphicsPixmapItem):
    pass


class Object(QGraphicsPixmapItem):

    def __init__(self, sample: Object, left: int, top: int, image_path: str = None) -> object:
        if sample is  not None:
            # Creating copy for plane
            self._path = sample._path
            super().__init__(sample.pixmap().copy())
            self._gen_connections(sample.childItems())
            self.setPos(left, top)

        else:
            # Creating Sample
            self._path = image_path
            image = QImage(self._path)
            if image.isNull():
                print("Eror while loading image:", self._path)
            super().__init__(QPixmap(image))

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, True)

    def add_connection(self, connection: IOBase):
        connection.setParentItem(self)

    def link_untyped(self):
        untyped_ones = []

        for connection in self._connections:
            if connection.iotype is IOType.UNTYPED:
                untyped_ones.append(connection)

        for connection in untyped_ones[1:]:
            untyped_ones[0].link(connection)

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        super().mouseMoveEvent(event)
        
        for con in self.childItems():
            con.load()

    def _gen_connections(self, connections: []):
        untyped_ones = []

        for connection in connections:
            new_connection = IODefined(connection.iotype, connection.x(), connection.y())
            new_connection.setParentItem(self)
            if new_connection.iotype is IOType.UNTYPED:
                untyped_ones.append(new_connection)

        for connection in untyped_ones[1:]:
            untyped_ones[0].link(connection)

    def __getstate__(self):

        children = map(pickle.dumps, self.childItems())

        return "obj", self.x(), self.y(), self._path, children

    def __setstate__(self, state):
        print("reading")
        if state[0] == "obj":
            Object.__init__(self, None, state[1], state[2], state[3])

            is_undef = False
            for children in state[4]:
                con = pickle.loads(children)
                self.add_connection(con)
                if isinstance(con, IOUndefined):
                    is_undef = True

            if is_undef:
                childrens = self.childItems()
                for child in childrens[1:]:
                    childrens[0].link(child)

        else:
            print("Error while reading")

