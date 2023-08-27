import sys
from drawboardwindow import DrawBoardWindow
from PyQt6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = DrawBoardWindow()

    sys.exit(app.exec())


main()



