from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsLineItem
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QLine
from enum import Enum


class Line(QGraphicsLineItem):

    _con1 = None
    _con2 = None

    def __init__(self, con1: QGraphicsPixmapItem, con2: QGraphicsPixmapItem = None):
        super().__init__(con1)
        self._con1 = con1
        self._con2 = con2
        if self._con2 is not None:
            self.load()
        pass

    def load(self, x=None, y=None):
        if x is None:
            self.setLine(15, 15, self._con2.scenePos().x() - self._con1.scenePos().x() + 15, self._con2.scenePos().y() - self._con1.scenePos().y() + 15)
        else:
            # print("Mouse moving")
            self.setLine(15, 15, x - self._con1.scenePos().x() + 0, y - self._con1.scenePos().y() + 0)
