from objects.connections.io_types import IOTypes
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from abc import ABC, abstractmethod


class IOAbc(ABC):
    pass


class IOAbc(QGraphicsPixmapItem):
    connection = None
    iotype = None
    image = QImage("images/others/connection.png")

    def __init__(self, left, top):
        super().__init__(QPixmap.fromImage(self.image))
        self.setPos(left, top)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, True)

    @abstractmethod
    def connect(self, other_io: IOAbc):
        pass

    @abstractmethod
    def _connection(self, first: IOAbc):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def _disconnect(self):
        pass

