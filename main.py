import sys

from plane_window import PlaneWindow
from PyQt6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = PlaneWindow()

    sys.exit(app.exec())


main()
