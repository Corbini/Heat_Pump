from objects.connections.io_abc import IOAbc
from objects.connections.io_types import IOTypes


class IODefined(IOAbc):

    def __init__(self, iotype: IOTypes):
        self.connection = None
        self.iotype = iotype

    # class tries to connect and output if it connected
    def connect(self, other_io: IOAbc):
        self.disconnect()

        if other_io._connection(self) is False:
            return False

        self.connection = other_io
        print("Connected")
        return True

    def _connection(self, first: IOAbc):
        if self.connection is not None:
            return False

        if self.iotype is not first.iotype and not \
                (first.iotype is IOTypes.UNTYPED or self.iotype is IOTypes.UNTYPED):
            print("Can't connect: bad types")
            return False

        self.connection = first
        return True

    def disconnect(self):
        if self.connection is None:
            return False

        self.connection._disconnect()
        self._disconnect()
        return True

    def _disconnect(self):
        self.connection = None
        print("Disconnected")
