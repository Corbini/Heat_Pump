from connector.connector_type import ConnectorType, Pointed
from connector.connector_graphic import ConnectorGraphic


class Connector:
    pass


class Connector:

    def __init__(self, x, y, identity,
                 io_type: ConnectorType = ConnectorType.UNTYPED,
                 pointed: Pointed = Pointed.LEFT, linked: Connector = None):
        self.__interface = None
        self.__x = x
        self.__y = y
        self.type = io_type
        self.__pointed = pointed
        self.linked = linked
        self.__identity = identity

    def __setstate__(self, state):
        if state[0] == "io":
            Connector.__init__(self, state[1], state[2], state[3], state[4], state[5], state[6])

    def __getstate__(self):
        if self.__interface is not None:
            self.__x = self.__interface.x()
            self.__y = self.__interface.y()

        return "io", self.__x, self.__y, self.__identity, self.type, self.__pointed, self.linked

    def show_on_screen(self, parent, obj_id):
        self.__interface = ConnectorGraphic(parent, self.__x, self.__y, self.type.path(),
                                            self.__pointed, obj_id, self.__identity)

    def get_interface(self):
        return self.__interface

    def identity(self):
        return self.__identity

    def io_type(self):
        return self.type

    @staticmethod
    def check_link(self, pointed: Connector):
        if pointed is None:
            return False

        if issubclass(pointed.__class__, Connector) is False:
            return False

        if self.type == ConnectorType.UNTYPED:
            return True

        if pointed == ConnectorType.UNTYPED:
            return True
        if self.type == pointed.io_type():
            return True

        return False

    def __link(self, other_io: Connector):
            self.__linked = other_io
            if self.type is ConnectorType.UNTYPED:
                self.type = other_io.io_type()

    def link(self, other_io: Connector):
        if other_io.linked is self:
            self.__link(other_io)
            self.__check_type(other_io)

        status = self.check_link(self, other_io)
        if status is False:
            return False

        self.__link(other_io)
        self.__check_type(other_io)
        return True

    def __check_type(self, other_io: Connector):
        if other_io.io_type() == ConnectorType.UNTYPED:
            return

        if self.type != ConnectorType.UNTYPED:
            return

        self.type = other_io.io_type()
        self.__interface.change_image(self.type.path())

    def unlink(self, change: bool = False):
        if change:
            self.type= ConnectorType.UNTYPED

        if self.linked() is not None:
            self.linked().unlink()
            self.__linked = None
