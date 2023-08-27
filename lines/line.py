from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsLineItem


class Line(QGraphicsLineItem):

    _connected_from = None
    _connected_to = None

    def __init__(self, con_from: QGraphicsPixmapItem, con_to: QGraphicsPixmapItem = None):
        super().__init__()
        self._connected_from.scene().addLine(self)
        self._connected_from = con_from
        self._connected_to = con_to
        self.load()

    def load(self, x=None, y=None):
        self.setLine(15, 15, self._con2.scenePos().x() - self._con1.scenePos().x() + 15,
                     self._con2.scenePos().y() - self._con1.scenePos().y() + 15)

    def check_object(self, object):
        if self._connected_from is object:
            return True
        if self._connected_to is object:
            return True

        return False