# class for additional heat source elements
from PyQt6.QtWidgets import QListWidget, QLabel
from PyQt6.QtGui import *
from ioobjects import *


class HeatSource(QLabel):


    def __init__(self, parent):
        super().__init__(parent)
        self._load_list()

    def _load_list(self):
        pass

    def drop(self):
        pass


