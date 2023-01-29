from ioobjects.bases.io_base import IOBase
from ioobjects.bases.io_type import IOType
from ioobjects.bases.io_drag_line import DragLine

# PyQt
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsSceneMouseEvent
from PyQt6.QtGui import QImage, QPixmap, QTransform

from abc import abstractmethod
from enum import Enum


class Pointed(Enum):
    TOP = 0
    RIGHT = 90
    BOTTOM = 180
    LEFT = 270


class IOGraphic(QGraphicsPixmapItem, DragLine, IOBase):

    _connection_line = None
    _line = None

    def __init__(self, parent: QGraphicsPixmapItem, x, y, iotype: IOType, pointed: Pointed):
        # QGraphicsPixmapItem has super therefor it init Dragline
        QGraphicsPixmapItem.__init__(self, parent, io_from=self)
        self.pointed = pointed
        """
        self.setTransformOriginPoint(15, 15)
        self.setRotation(pointed.value)"""
        IOBase.__init__(self, x, y, iotype)

        self.set_image()

        self.setPos(x, y)

    def set_image(self):

        image = QPixmap(QImage(self._iotype.path()))

        transform = QTransform()
        transform.translate(15, 15)
        transform.rotate(self.pointed.value)
        image = image.transformed(transform)

        if image.isNull():
            print("Error while reading data")
        self.setPixmap(image)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.check_pressed(event)

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.check_move(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.check_release():
            # Find Pointed Object
            pos = event.scenePos()
            pointed = self.scene().itemAt(pos, self.transform())
            # Check object
            if pointed is not None:
                if issubclass(pointed.__class__, IOBase):
                    self.connect(pointed)

    @abstractmethod
    def __getstate__(self):
        self._x = self.x()
        self._y = self.y()
        state = IOBase.__getstate__(self), self.pointed
        return state

    @abstractmethod
    def __setstate__(self, state):
        new_iobase = state[0]
        new_pointed = state[1]

        if new_iobase[0] == "io":
            IOGraphic.__init__(self, None, new_iobase[1], new_iobase[2], new_iobase[3], new_pointed)
        else:
            print("Error while reading")

    def _gen_line(self):
        pass

    def load(self):
        if self._line is not None:
            self._line.load()
    @abstractmethod
    def connect(self, other_io: IOBase) -> bool:
        return False

    @abstractmethod
    def _connection(self, first: IOBase) -> bool:
        return False

    @abstractmethod
    def disconnect(self):
        return False

    @abstractmethod
    def _disconnect(self):
        return False
