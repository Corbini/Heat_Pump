from io_defined import IODefined


class IOUndefined(IODefined):

    def __init__(self, iotype):
        super(IODefined, self).__init__(iotype)
        self.connection = None
        self.iotype = iotype

    # class tries to connect and output if it connected
    def connect(self, other_io):
        if self.connection is not None:
            self.connection.connection_break()
            self.connection = None

        if other_io.connect_to(self) is False:
            return False

        self.connection = other_io
        return True

    def connect_to(self, first):
        if self.connection is not None and self.iotype is first.iotype:
            return False

        self.connection = first
        return True

    def connection_break(self):
        self.connection.broken()
        self.broken()

    def broken(self):
        self.connection = None
