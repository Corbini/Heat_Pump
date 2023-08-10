import pickle

from PyQt6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem, QGraphicsScene
from PyQt6.QtGui import QPixmap, QImage
from ioobjects.bases import *
from ioobjects import *

from pathlib import Path
from file import save_obj


class ObjectInterface(QGraphicsPixmapItem):
    pass


class ObjectInterface(QGraphicsPixmapItem):

    def __init__(self, sample: ObjectInterface, left: int, top: int, image_path: str = None) -> object:
        if sample is  not None:
            # Creating copy for plane
            self._path = sample._path
            super().__init__(sample.pixmap().copy())
            self._gen_connections(sample.childItems())
            self.setPos(left, top)
            self.__identity_number = -1

        else:
            # Creating Sample
            self._path = image_path
            image = QImage(self._path)
            if image.isNull():
                print("Eror while loading image:", self._path)
            super().__init__(QPixmap(image))

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, True)

    def set_xy(self, position_x, position_y):
        self.setX(position_x)
        self.setY(position_y)

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        super().mouseMoveEvent(event)

        for con in self.childItems():
            con.load()

    def add_connection(self, connection: IOBase):
        connection.setParentItem(self)



class Object:

    def __init__(self, image_path: str = None, connector_change = False, left: int = 0, top:\
            int = 0, identity_number: int = -1) -> object:

        self.__connection_counter = 0
        self.__connectors = list()

        self.__connection_change = connector_change
        self.__image_path = image_path
        self.__pos_x = left
        self.__pos_y = top
        self.__identity_number = identity_number

        self.__interface = None

    def show(self):
        if self.__interface is not None:
            del self.__interface
        self.__interface = ObjectInterface(None, self.__pos_x, self.__pos_y, self.__image_path)
        for connector in self.__connectors:
            connector.setParentItem(self.__interface)

    def add_io_defined(self, x, y, iotype: IOType, pointed: Pointed):

        self.__connectors.append(IODefined(None, x, y, iotype, pointed))
        self.__connection_counter += 1

    def add_io_undefined(self, x, y, pointed: Pointed):
        self.__connectors.append(IOUndefined(None, x, y, pointed))
        self.__connection_counter += 1
        self.__connection_change = True

    def link_untyped(self):
        untyped_ones = []

        for connection in self._connections:
            if connection.iotype is IOType.UNTYPED:
                untyped_ones.append(connection)

        for connection in untyped_ones[1:]:
            untyped_ones[0].link(connection)

    def _gen_connections(self, connections: []):
        untyped_ones = []

        for connection in connections:
            new_connection = IODefined(connection.iotype, connection.x(), connection.y())
            new_connection.setParentItem(self)
            if new_connection.iotype is IOType.UNTYPED:
                untyped_ones.append(new_connection)

        for connection in untyped_ones[1:]:
            untyped_ones[0].link(connection)

    def __getstate__(self):
        children = map(pickle.dumps, self.__connectors)

        return "obj", self.__image_path, self.__connection_change, self.__pos_x,\
            self.__pos_y, self.__identity_number, children

    def __setstate__(self, state):
        print("reading")
        if state[0] == "obj":
            Object.__init__(self, state[1], state[2], state[3], state[4], state[5])

            is_undef = False
            for children in state[6]:
                print(children)
                con = pickle.loads(children)
                self.__connectors.append(con)
                if isinstance(con, IOUndefined):
                    is_undef = True

            # if is_undef:
            #     childrens = self.__interface.childItems()
            #     for child in childrens[1:]:
            #         childrens[0].link(child)

        else:
            print("Error while reading")

    def sample(self):
        # link all undef connection
        first_undef = None
        for child in self.__connectors:
            if isinstance(child, IOUndefined):
                if first_undef is None:
                    first_undef = child
                else:
                    first_undef.link(child)

        image_path = Path(self.__image_path)
        path = Path(image_path.stem + ".io")

        save_obj(self, str(path))

    def add_on_scene(self, position_x, position_y, identity_number, view):
        self.__pos_x = position_x
        self.__pos_y = position_y
        self.show()
        view.addItem(self.__interface)
        self.__identity_number = identity_number

    def id(self):
        return self.__identity_number
