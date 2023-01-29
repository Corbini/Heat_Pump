import pickle

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import *

class Sample(QLabel):

    _name = ""

    def __init__(self, parent: QWidget, path_to_sample: str, name: str):
        super().__init__(parent)
        self._path = path_to_sample
        self.setFrameStyle(QFrame.Shape.StyledPanel)
        self.setText(name)
       # self.setPixmap(QPixmap("images/heat_pumps/Gree_Split.png"))
        # if self.pixmap().isNull():
        #     print("images/heat_pumps/Gree_Split.png", " can't be loaded")
        self._name = self.text()
        self.setToolTip(name)
        self.show()

    def mousePressEvent(self, mouse: QMouseEvent):
        if mouse.buttons() is Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            drag.setMimeData(mime_data)
            mime_data.setText(self._path)
            drag.setPixmap(self.pixmap())
            # drag.setHotSpot(mouse.position().toPoint() - self.rect().topLeft())
            dropAction = drag.exec()
