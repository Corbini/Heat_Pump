from enum import Enum
from abc import *
from dataclasses import dataclass


class Event(Enum):
    CONNECT_ID = 0
    DISCONNECT_ID = 1
    REMOVE_ID = 2
    ADD_OBJ = 3
    MOVE_OBJ = 4
    REMOVE_OBJ = 5
    UPDATE_IMG = 6


class AddObj:
    file_name = ""
    left = 0
    top = 0


class AddHandler(ABC):
    @abstractmethod
    def add_obj(self, data: AddObj):
        pass


class Caller:
    __event_process = None

    @classmethod
    def set_event_process(cls, event_process):
        cls.__event_process = event_process

    @classmethod
    def set_event_process(cls, event_process):
        cls.__event_process = event_process

    def call(self, event: Event, data):
        self.__event_process.call(event, data)


class Connection:
    def __init__(self):
        self.__pool = None

    def pool(self):
        return self.__pool

    def set_pool(self, pool):
        self.__pool = pool


class EventProcess(ABC):
    @abstractmethod
    def call(self, event: Event, data):
        pass
