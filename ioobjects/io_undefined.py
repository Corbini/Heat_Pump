import pickle

from ioobjects.bases import *
from PyQt6.QtWidgets import QGraphicsPixmapItem


class IOUndefined(IOGraphic):
    pass


class IOUndefined(IOGraphic, IOLink):

    def __init__(self, parent: QGraphicsPixmapItem, x, y, pointed=Pointed.LEFT):
        IOGraphic.__init__(self, parent, x, y, IOType.UNTYPED, pointed)
        IOLink.__init__(self)

    def __setstate__(self, state):
        if state[0] == "ioun":
            IOGraphic.__setstate__(self, state[1])
            self._links = state[2]

    def __getstate__(self):
        return "ioun", IOGraphic.__getstate__(self), self._links

    def connect(self, other_io: IOBase):
        self.disconnect()

        if other_io._connection(self) is False:
            return False

        self._connectedIO = other_io
        print("Connected points")

        if self._iotype is IOType.UNTYPED:
            self.set_link_type(other_io._iotype)

        # Create Visual connection
        self._gen_line()

        return True

    def _connection(self, first: IOBase):
        if self._connectedIO is not None:
            return False

        if self._iotype is not first._iotype and not\
                (first._iotype is IOType.UNTYPED or self._iotype is IOType.UNTYPED):
            print("Can't connect: bad types")
            return False

        self._connectedIO = first

        if self._iotype is IOType.UNTYPED:
            self.set_link_type(first._iotype)

        return True

    def disconnect(self):
        if self._connectedIO is None:
            return False

        self._connectedIO._disconnect()
        self._disconnect()
        return True

    def _disconnect(self):
        self._connectedIO = None
        self.check_link_type()
        del self.connection
