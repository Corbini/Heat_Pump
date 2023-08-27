from connector.graphic_drag_line import DragLine
from connector.connector_type import Pointed, ConnectorType
from eventhandler import Caller, Event, Identity
from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsSceneMouseEvent
from PyQt6.QtGui import QImage, QPixmap, QTransform


class ConnectorGraphic(QGraphicsPixmapItem, Caller, Identity):

    def __init__(self, object_interface, x, y, image_path, pointed: Pointed,
                 obj_id, con_id):
        image = self.__load_pixmap(image_path, pointed)

        QGraphicsPixmapItem.__init__(self, image, object_interface)
        Identity.__init__(self, obj_id, con_id)

        self.setPos(x, y)

        self.__drag_line = DragLine(self)

    @staticmethod
    def __load_pixmap(path, pointed):
        image = QPixmap(QImage(path))

        transform = QTransform()
        transform.translate(15, 15)
        transform.rotate(pointed.value)
        image = image.transformed(transform)
        return image

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.__drag_line.check_pressed(event)

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.__drag_line.check_move(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.__drag_line.check_release():
            # Find Pointed Object
            pos = event.scenePos()
            pointed = self.scene().itemAt(pos, self.transform())
            # Check object
            if pointed is None:
                return

            if isinstance(pointed, ConnectorGraphic):
                print({self, pointed})
                self.call(Event.CONNECT_ID, [self, pointed])

    def __del__(self):
        self.call(Event.DISCONNECT_ID, self)

    def show_on_screen(self, parent):
        self.setParentItem(parent)

    def change_image(self, connector_type: ConnectorType):
        self._path = connector_type.path()
        image = QImage(self._path)
        self.setPixmap(image)

        self.call(Event.UPDATE_IMG, [self, connector_type])
