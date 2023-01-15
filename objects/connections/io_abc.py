from objects.connections.io_types import IOTypes
from abc import ABC, abstractmethod

class IOAbc(ABC):
    pass


class IOAbc(ABC):
    connection = None
    iotype = None


    @abstractmethod
    def connect(self, other_io: IOAbc):
        pass


    @abstractmethod
    def _connection(self, first: IOAbc):
        pass


    @abstractmethod
    def disconnect(self):
        pass


    @abstractmethod
    def _disconnect(self):
        pass

