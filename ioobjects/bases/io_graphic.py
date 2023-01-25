from ioobjects.bases.io_base import IOBase
from ioobjects.bases.io_type import IOType
from ioobjects.bases.io_drag_line import DragLine

# PyQt
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsSceneMouseEvent
from PyQt6.QtGui import QImage, QPixmap

from abc import abstractmethod


class IOGraphic(QGraphicsPixmapItem, DragLine, IOBase):

    _connection_line = None
    _line = None

    def __init__(self, parent: QGraphicsPixmapItem, x, y, iotype: IOType):
        # QGraphicsPixmapItem has super therefor it init Dragline
        QGraphicsPixmapItem.__init__(self, parent, io_from=self)
        IOBase.__init__(self, x, y, iotype)

        image = QPixmap(QImage(self._iotype.path()))
        if image.isNull():
            print("Error while reading data")
        self.setPixmap(image)

        self.setPos(x, y)

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

    def __getstate__(self):
        self._x = self.x()
        self._y = self.y()
        return IOBase.__getstate__(self)

    def __setstate__(self, state):
        if state[0] == "io":
            self.__init__(None, state[1], state[2], state[3])
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
