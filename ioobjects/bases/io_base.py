from ioobjects.bases.io_type import IOType
from abc import abstractmethod


class IOBase:
    pass


class IOBase:
    _connectedIO = None

    def __init__(self, x: int, y: int, iotype: IOType):
        self._x = x
        self._y = y
        self._iotype = iotype

    def __getstate__(self):
        return "io", self._x, self._y, self._iotype

    def __setstate__(self, state):
        if state[0] is "io":
            self.__init__(state[1], state[2], state[3])
        else:
            print("Error while reading")

    @abstractmethod
    def connect(self, other_io: IOBase) -> bool:
        return False

    @abstractmethod
    def _connection(self, first: IOBase) -> bool:
        return False

    @abstractmethod
    def disconnect(self):
        return False

    @abstractmethod
    def _disconnect(self):
        return False
