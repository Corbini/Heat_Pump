from PyQt6.QtWidgets import QApplication
import sys

from window import Window


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        game = Window(self)
        self.exec()
