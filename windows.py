from PyQt6.QtWidgets import QLabel, QMainWindow
from PyQt6.QtGui import *


class Window(QMainWindow):
    def __init__(self, q_app):
        # pyqt6 init
        self.app = q_app
        super().__init__()

        # window setup
        self.setWindowTitle("Projekty")
        self.setWindowIcon(QIcon('images/Logo.png'))
        self.setFixedSize(1280, 960)
        self.background = QLabel()
        self.setCentralWidget(self.background)
        self.show()
