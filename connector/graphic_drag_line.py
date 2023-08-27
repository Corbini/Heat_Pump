from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsLineItem, QGraphicsSceneMouseEvent
from PyQt6.QtCore import Qt


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
        transform =  self._io_from.transformOriginPoint()
        self._line_item.setLine(io_pos.x() + 15, io_pos.y() + 15, mouse_pos.x(),
                                mouse_pos.y())

    def check_release(self) -> bool:
        if self._line_item is None:
            return False

        self._io_from.scene().removeItem(self._line_item)
        self._line_item = None

        return True
