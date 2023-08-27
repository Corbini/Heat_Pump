import pickle
from toolbox.gen_samples import gen_obj
from drawboard.drawboardinterface import DrawBoardInterface
from object.onboard import OnBoard
from eventhandler.eventinterface import AddObj, AddHandler
from eventhandler.objecthandle import Dictionary, Identity
from eventhandler.eventhandler import EventHandler
from object import Object
from file import load_obj


class DrawBoard(AddHandler):

    def __init__(self):
        self.__interface = DrawBoardInterface()
        self.__event_process = EventHandler(self)
        OnBoard.set_board(self.__interface.plane)
        self.__dictionary = Dictionary()

        gen_obj()

    def set_window(self, window):
        self.__interface.set_window(window)

    def set_view_size(self, left: int, top: int, width: int, height: int):
        self.__interface.set_view_size(left, top, width, height)

    def new(self):
        for child in self.__interface.children():
            del child

        Dictionary.clear()

    def __getstate__(self):

        return "brd", Dictionary

    def __setstate__(self, state):
        self.__init__()
        print("reading")
        if state[0] == "brd":
            DrawBoard()

    def add_to_board(self, obj: Object, left=-1, top=-1):

        # find empty slot
        identity = self.__dictionary.find_slot()
        if identity is None:
            print("Failed to add")
            return None

        obj.show_on_screen(identity, left, top)
        self.__dictionary.add(obj, identity)

        return Identity(identity)

    def __get_id(self):
        return None

    def add_obj(self, add_obj: AddObj):
        obj = load_obj(add_obj.file_name)

        self.add_to_board(obj, add_obj.left, add_obj.top)

    def remove_from_board(self, item):
        self.__dictionary.remove(item.id())

    def __add_to_board_at(self, item, identity_number):
        self.__dictionary.add(item, identity_number)

    def delete(self):
        pass
