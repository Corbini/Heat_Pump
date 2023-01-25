# class for toolbox and its category
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from toolbox import *

# class for plane ToolBox and its menu
class ToolBox(QWidget):

    def __init__(self):
        # Window properties
        super().__init__()
        self.resize(300, 900)
        self.setWindowTitle("Toolbox")
        self.setWindowIcon(QIcon("../images/Logo.png"))

        # Show it on screen
        self.show()
        self.tests()

    def tests(self):
        sample = Sample(self, "images/heat_pumps/Gree_Split.png", "Gree Split")