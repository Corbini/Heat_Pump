from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from toolbox import *
from pathlib import Path
import os


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
        # self.tests()
        self.load_from_files()

    def load_from_files(self):
        path = Path("data")
        dir_list = os.listdir(path)
        for file in dir_list:
            print(file)
            self.load_file(file)

    def load_file(self, file_name: str):
        name_ex = file_name.split('.')
        name = name_ex[0]
        name = name.replace('_', " ")
        sample = Sample(None, file_name, name)
        self.layout().addWidget(sample)
