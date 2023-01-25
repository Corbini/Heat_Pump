from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsLineItem, QGraphicsScene, QGraphicsSceneMouseEvent
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QLine
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QEvent


class DragLine:

    _io_from = None
    _line_item = None

    def __init__(self, io_from: QGraphicsPixmapItem):
        self._io_from = io_from

    def check_pressed(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.buttons() is Qt.MouseButton.LeftButton:
            self._line_item = QGraphicsLineItem()
            self._io_from.scene().addItem(self._line_item)
            self.update_line(event)

    def check_move(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.buttons() is Qt.MouseButton.LeftButton and self._line_item is not None:
            self.update_line(event)

    def update_line(self, event: QGraphicsSceneMouseEvent):
        mouse_pos = event.scenePos()
        io_pos = self._io_from.scenePos()
        self._line_item.setLine(15 + io_pos.x(), 15 + io_pos.y(), mouse_pos.x(),
                                mouse_pos.y())

    def check_release(self) -> bool:
        if self._line_item is None:
            return False

        self._io_from.scene().removeItem(self._line_item)
        self._line_item = None

        return True