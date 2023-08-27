import pickle

from connector import Connector, Pointed, ConnectorType
from eventhandler import Caller, EventProcess, Event, Identity, DictionaryObject
from object.object_interface import ObjectInterface
from pathlib import Path
from file import save_obj


class Object:
    pass


class Object(Caller, DictionaryObject):

    def __init__(self, image_path: str, connector_change: bool = False, left: int = None,
                 top: int = None, obj_id: int = None):

        self.__interface = None
        self.__connection_counter = 0
        self.__connectors = list()
        self.__connection_change = connector_change

        self.__image_path = image_path
        self.__pos_x = left
        self.__pos_y = top
        self.__identity = obj_id

        self.group = None

    def __del__(self):
        del self.__interface

    def show_on_screen(self, identity: Identity, x=-1, y=-1):
        if self.__identity is None:
            self.__identity = identity
        if self.__pos_x is None:
            self.__pos_x = x
        if self.__pos_y is None:
            self.__pos_y = y

        self.__interface = ObjectInterface(self.__pos_x, self.__pos_y, self.__image_path, self.__identity)

        for connector in self.__connectors:
            connector.show_on_screen(self.__interface, self.__identity)

    def add_connector(self, x, y, iotype: Connector, pointed: Pointed):
        connector = Connector(x, y, self.__connection_counter, iotype, pointed, None)
        self.__connectors.append(connector)
        self.__connection_counter += 1

    def __getstate__(self):
        children = map(pickle.dumps, self.__connectors)
        if self.__interface is not None:
            self.__pos_x = self.__interface.x()
            self.__pos_y = self.__interface.y()

        return "obj", self.__image_path, self.__connection_change, self.__pos_x,\
            self.__pos_y, self.__identity, children

    def __setstate__(self, state):
        print("reading")
        if state[0] == "obj":
            print("state is correct")
            self.__init__(state[1], state[2], state[3], state[4], state[5])

            is_undef = False
            for children in state[6]:
                print(children)
                con = pickle.loads(children)
                self.__connectors.append(con)

        else:
            print("Error while reading")

    def connector_at(self, io_id):
        return self.__connectors[io_id]

    def sample(self):
        image_path = Path(self.__image_path)
        path = Path(image_path.stem + ".io")
        self.__identity = None

        save_obj(self, str(path))

    def add_on_scene(self, position_x, position_y, identity, view):
        self.__pos_x = position_x
        self.__pos_y = position_y
        self.show()
        view.addItem(self.__interface)
        self.__identity = identity

    def identity(self):
        return self.__identity

    def link(self, other_obj: Object, con_id, other_con_id):
        status = self.__connectors[con_id].link(other_obj.connector_at(other_con_id))
        if status:

            self.__connectors[con_id].linked = Identity(other_obj.identity(), other_con_id)
            other_obj.connector_at(other_con_id).linked = Identity(self.__identity, con_id)

        return status

    def delink(self, other_obj: Object):
        return False

    def get_connectors(self):
        return self.__connectors

    def update_type(self, type):
        if self.__connection_change:
            for con in self.__connectors:
                con.type = type
