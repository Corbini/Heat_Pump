from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.Qt6 import *
from toolbox import ToolBox
from plane import Plane


# class for plane window and its menu
class PlaneWindow(QMainWindow):

    def __init__(self):
        # Window properties
        super().__init__()
        self.resize(900, 900)
        self.setWindowTitle("Widok Projektu")
        self.setWindowIcon(QIcon("images/Logo.png"))

        self._create_menubar()

        # Create Plane
        self.plane = Plane(self)
        self._set_plane()
        self.plane.load()

        # Create toolbox
        self.toolbox = ToolBox()

        # Show it on screen
        self.show()

    def _set_plane(self):
        self.plane.setGeometry(0, self.menubar.size().height(),
                               self.size().width(), self.size().height() - self.menubar.size().height())

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self._set_plane()

    def _create_menubar(self):
        self.menubar = QMenuBar(self)

        self.extract = QAction("Extract", self)
        self.extract.setShortcut("Ctrl+E")
        self.menubar.addAction(self.extract)

        self.save = QAction("Save", self)
        self.save.setShortcut("Ctrl+S")
        self.menubar.addAction(self.save)

        self.load = QAction("Load", self)
        self.load.setShortcut("Ctrl+S")
        self.menubar.addAction(self.load)

        self.setMenuBar(self.menubar)

    def __del__(self):
        del self.toolbox
        del self.menubar

    def closeEvent(self, event):
        self.toolbox.deleteLater()

    def processtrigger(self, q):
        print(q.text()+" is triggered")
