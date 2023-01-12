from PyQt6.QtWidgets import QApplication
import sys

from windows import Window


class Application(QApplication):
    def __init__(self):
        # pyqt6 init
        super().__init__(sys.argv)

        game = Window(self)
        self.exec()
