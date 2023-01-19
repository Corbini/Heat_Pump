from PyQt6.QtWidgets import QLabel, QGraphicsPixmapItem, QGraphicsItem, QGraphicsSceneMouseEvent
from PyQt6.QtGui import *
from PyQt6.QtCore import QPointF
from abc import ABC, abstractmethod
from objects.connections.line import Line
from PyQt6.QtCore import Qt, QMimeData




class IOAbc(QGraphicsPixmapItem):
    pass


class IOAbc(QGraphicsPixmapItem):
    connection = None
    iotype = None
    image = QImage("images/others/connection.png")
    _line = None
    _drag_line = None

    def __init__(self, left, top):
        super().__init__()
        self.setPixmap(QPixmap.fromImage(self.image))
        self.setPos(QPointF(left, top))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, False)

    def _gen_line(self):
        self._line = Line(self, self.connection)
        self.connection._line = self._line
        # self._line.setParentItem(self)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        if event.buttons() is Qt.MouseButton.LeftButton:
            self._drag_line = Line(self)

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:

        if event.buttons() is Qt.MouseButton.LeftButton:
            self._drag_line.load(event.scenePos().x(), event.scenePos().y())

    def mouseReleaseEvent(self, ev: QGraphicsSceneMouseEvent) -> None:
        if self._drag_line is not None:
            # Delete drag line
            self._drag_line.setParentItem(None)
            self._drag_line = None
            # Find Pointed Object
            pos = ev.scenePos()
            pointed = self.scene().itemAt(pos, self.transform())
            # Check object
            if pointed is not None:
                if issubclass(pointed.__class__, IOAbc):
                    self.connect(pointed)

    def load(self) -> None:
        if self._line is not None:
            self._line.load()

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

