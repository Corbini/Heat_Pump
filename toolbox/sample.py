import pickle

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import *


class Sample(QLabel):

    _name = ""

    def __init__(self, parent: QWidget, path_to_image: str, name: str):
        super().__init__(parent)
        self.setPixmap(QPixmap(path_to_image))
        if self.pixmap().isNull():
            print(path_to_image, " can't be loaded")
        self._name = name
        self.setToolTip(name)
        self.show()

    def mouseMoveEvent(self, mouse: QMouseEvent):
        if mouse.buttons() is Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            drag.setMimeData(mime_data)
            mime_data.setText(self._name)
            drag.setPixmap(self.pixmap())
            drag.setHotSpot(mouse.position().toPoint() - self.rect().topLeft())
            dropAction = drag.exec()

    def dragMoveEvent(self, dragging: QDragMoveEvent):
        print("LOL")