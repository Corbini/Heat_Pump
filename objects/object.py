from objects.connections.io_abc import IOAbc
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem, QGraphicsScene
from PyQt6.QtGui import QPixmap, QImage
from objects.connections import *


class Object(QGraphicsPixmapItem):

    def __init__(self, sample: QGraphicsPixmapItem, left, top, image: QImage = None):
        if image is None:
            # Creating copy for plane

            super().__init__(sample.pixmap().copy())
            self._gen_connections(sample.childItems())
            self.setPos(left, top)

        else:
            # Creating Sample
            super().__init__(QPixmap(image))
            print("Load Sample")

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, True)

    def add_connection(self, connection: IOAbc):
        connection.setParentItem(self)

    def link_untyped(self):
        untyped_ones = []

        for connection in self._connections:
            if connection.iotype is IOTypes.UNTYPED:
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
            if new_connection.iotype is IOTypes.UNTYPED:
                untyped_ones.append(new_connection)

        for connection in untyped_ones[1:]:
            untyped_ones[0].link(connection)
