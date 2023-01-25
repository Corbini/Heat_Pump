from PyQt6.QtWidgets import QGraphicsPixmapItem
from ioobjects.bases.io_type import IOType


class IOLink:
    pass


class IOLink:

    _links = []
    _connectedIO = None
    _iotype = IOType.UNTYPED

    def link(self, other_io: IOLink):
        self._links.extend(other_io._links)
        for io_others_linked in other_io._links:
            io_others_linked._links = self._links

    def _check_connection(self):
        for io_linked in self._links:
            if io_linked._connectedIO is not None:
                return True

        return False

    def set_link_type(self, iotype):
        for io_linked in self._links:
            io_linked._iotype = iotype

    def check_link_type(self):

        if self._check_connection():
            return

        self.set_link_type(IOType.UNTYPED)






