from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from toolbox.toolbox import ToolBox
from drawboard import DrawBoard
from window import Window


class DrawBoardWindow(QMainWindow):

    def __init__(self):
        # Window properties
        super().__init__()
        self.resize(900, 900)
        self.setWindowTitle("Widok Projektu")
        self.setWindowIcon(QIcon("images/Logo.png"))
        self.acceptDrops()

        self.__create_menubar()
        # Create Plane
        self.draw_board = DrawBoard()
        self.draw_board.set_window(self)
        # Create toolbox
        self.toolbox = ToolBox()

        # Show it on screen
        self.show()

    def __set_plane(self):
        self.draw_board.set_view_size(0, self.menubar.size().height(),
                                       self.size().width(), self.size().height() - self.menubar.size().height())

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self.__set_plane()

    def __create_menubar(self):
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
