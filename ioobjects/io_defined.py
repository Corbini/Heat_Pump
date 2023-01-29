from ioobjects.bases import *
from PyQt6.QtWidgets import QGraphicsPixmapItem

class IODefined(IOGraphic):

    def __init__(self, parent: QGraphicsPixmapItem, x, y, iotype: IOType, pointed=Pointed.LEFT):
        IOGraphic.__init__(self, parent, x, y, iotype, pointed)

    # class tries to connect and output if it connected

    def __setstate__(self, state):
        if state[0] == "iodef":
            IOGraphic.__setstate__(self, state[1])

    def __getstate__(self):
        return "iodef", IOGraphic.__getstate__(self)

    def connect(self, other_io: IOType):
        self.disconnect()

        if other_io._connection(self) is False:
            return False

        self._connectedIO = other_io
        print("Connected")

        # Create Visual connection
        self._gen_line()
        return True

    def _connection(self, first: IOBase):
        if self._connectedIO is not None:
            return False

        if self._iotype is not first._iotype and not \
                (first._iotype is IOType.UNTYPED or self._iotype is IOType.UNTYPED):
            print("Can't connect: bad types")
            return False

        self._connectedIO = first
        return True

    def disconnect(self):
        if self._connectedIO is None:
            return False

        self._connectedIO._disconnect()
        self._disconnect()
        return True

    def _disconnect(self):
        self._connectedIO = None
        print("Disconnected")

