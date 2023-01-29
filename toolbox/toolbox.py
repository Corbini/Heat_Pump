# class for toolbox and its category
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from toolbox import *
from pathlib import Path


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
        self.setLayout(QHBoxLayout())
        self.tests()

    def add_sample(self, file_name, name):
        sample = Sample(None, str(file_name), name)
        self.layout().addWidget(sample)

    def tests(self):
        self.add_sample("Gree_Split.io", "Gree Split")
        self.add_sample("Kaisai_Split.io", "Kaisai Split")
        self.add_sample("Panasonic_Split.io", "Panasonic Split")
        self.add_sample("radiators.io", "Radiators")
        self.add_sample("Galmet_1_exchanger.io", "Galmet 1 Exchanger")
