from abc import *
import pickle

class Identity:
    def __init__(self, obj_id, io_id=-1):
        self.__obj_id = obj_id
        self.__io_id = io_id

    def io_id(self):
        return self.__io_id

    def obj_id(self):
        return self.__obj_id

    def __copy__(self):
        return Identity(self.__obj_id, self.__io_id)


class DictionaryObject(ABC):
    @abstractmethod
    def connector_at(self, io_id):
        return


class Dictionary(object):

    def __new__(cls):
        if not hasattr(cls, '__singleton'):
            cls.__singleton = super(Dictionary, cls).__new__(cls)
            cls.__dictionary = dict()
        return cls.__singleton

    @classmethod
    def __getstate__(cls):
        return "dict", cls.__dictionary

    @classmethod
    def __setstate__(cls, state):
        cls.__new__()
        print("reading")
        if state[0] == "dict":
            for item in state[1]:
                constructed_item = pickle.loads(item)
                identity = constructed_item.id()
                cls.add(constructed_item, identity)

    @classmethod
    def add(cls, data, identity: int):
        if identity < 0 or identity > 10000:
            raise Exception("identity not in brackets")

        if identity in cls.__dictionary:
            raise Exception("identity in use")

        cls.__dictionary[identity] = data
        return identity

    @classmethod
    def get(cls, obj_id):
        return cls.__dictionary[obj_id]

    @classmethod
    def get_con(cls, identity: Identity):
        obj = cls.get(identity.obj_id())
        return obj.connector_at(identity.io_id())

    @classmethod
    def clear(cls):
        del cls.__dictionary

        cls.__dictionary = dict()

    @classmethod
    def find_slot(cls):
        for identity in range(0, 10000):
            if identity not in cls.__dictionary:
                return identity
        return None

    @classmethod
    def remove(cls, identity: int):
        del cls.__dictionary[identity]
