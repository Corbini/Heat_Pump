from objects.connections.io_defined import IODefined
from objects.connections.io_types import IOTypes
from objects.connections.io_abc import IOAbc
from objects.connections.line import Line


class IOUndefined(IOAbc):
    pass


class IOUndefined(IOAbc):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.iotype = IOTypes.UNTYPED
        self.connection = None
        self.links = [self]
        print("IOUndefined Created")

    def connect(self, other_io: IOAbc):
        self.disconnect()

        if other_io._connection(self) is False:
            return False

        self.connection = other_io
        print("Connected points")

        if self.iotype is IOTypes.UNTYPED:
            self.set_link_type()

        # Create Visual connection
        self._gen_line()

        return True

    def _connection(self, first: IOAbc):
        if self.connection is not None:
            return False

        if self.iotype is not first.iotype and not\
                (first.iotype is IOTypes.UNTYPED or self.iotype is IOTypes.UNTYPED):
            print("Can't connect: bad types")
            return False

        if self.iotype is IOTypes.UNTYPED:
            self.set_link_type(first.iotype)
            self.connection = first

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

        connected_links = True
        for linked in self.links:
            if linked.connection is not None:
                connected_links = False
                print("Group connected to defined source")

        if connected_links:
            self.set_link_type(IOTypes.UNTYPED)

    def link(self, other_io: IOUndefined):
        self.links = other_io.links + self.links
        print("Created Link. Items in link:", len(self.links))

    def set_link_type(self, io_type: IOTypes):
        for linked in self.links:
            linked.iotype = io_type
        print("Group get a type", io_type)
