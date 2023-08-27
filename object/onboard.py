from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsScene


class OnBoard:
    __parent: QGraphicsScene = None

    @classmethod
    def set_board(cls, board_interface):
        cls.__parent = board_interface

    @classmethod
    def get_parent(cls):
        return cls.__parent
