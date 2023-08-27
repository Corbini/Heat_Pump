from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt6.QtGui import QPixmap, QImage
from eventhandler import Caller, EventProcess, Event, Identity
from object.onboard import OnBoard


class ObjectInterface(Caller, OnBoard, QGraphicsPixmapItem):

    def __init__(self, left: int, top: int, image_path: str, identity: Identity) -> object:
        self._path = image_path
        image = QImage(self._path)
        if image.isNull():
            print("Eror while loading image:", self._path)
        super().__init__(QPixmap(image))
        self.get_parent().addItem(self)
        self.show()

        self.setX(left)
        self.setY(top)

        self.__identity = identity

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, True)

    def get_position(self):
        return self.x(), self.y()

    def set_position(self, left, top):
        self.setX(left)
        self.setY(top)

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        super().mouseMoveEvent(event)
        self.call(Event.MOVE_OBJ, self.__identity)

    def add_connection(self, child: QGraphicsPixmapItem):
        child.setParentItem(self)
