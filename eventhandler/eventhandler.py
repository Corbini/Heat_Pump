from eventhandler.eventinterface import EventProcess, Connection, AddObj, Caller, AddHandler, Event
from eventhandler.objecthandle import Identity, Dictionary
from eventhandler.group import Group
from object.object import Object, ConnectorType


class EventHandler(EventProcess):

    def __init__(self, draw_board: AddHandler):
        Caller.set_event_process(self)

        self.__draw_board = draw_board
        self.__group = dict()

    def __new_group(self, data):
        pass

    def __connect_id(self, data: [Identity, Identity]):
        first_id: Identity = data[0]
        second_id: Identity = data[1]

        first_obj: Object = Dictionary.get(first_id.obj_id())
        second_obj: Object = Dictionary.get(second_id.obj_id())

        self.call(Event.DISCONNECT_ID, first_id)
        self.call(Event.DISCONNECT_ID, second_id)

        status = first_obj.link(second_obj, first_id.io_id(), second_id.io_id())

        if status:
            self.__connect_group(first_id, second_id)

    def __connect_group(self, first_id: Identity, second_id: Identity):
        first_obj = Dictionary.get(first_id.obj_id())
        second_obj = Dictionary.get(second_id.obj_id())

        if first_obj.group is None and second_obj.group is None:
            group_id = self.gen_group()
            group = self.__group[group_id]
            group.add(first_id, None)
            group.add(second_id, first_id)
            return

        if first_obj.group is None:
            second_obj.group.add(first_id, second_id)
            return

        if second_obj.group is None:
            first_obj.group.add(second_id, first_id)
            return

        first_obj.group.add_groups(second_obj.group)
        first_obj.group.gen_graphic(second_id, first_id)

    def gen_group(self):
        for group_number in range(10000):
            print(self.__group.get(group_number))
            if self.__group.get(group_number) is None:
                self.__group[group_number] = Group(group_number)
                return group_number
        return None

    def __disconnect_id(self, data):
        obj: Object = Dictionary.get(data.obj_id())
        if obj is None:
            "Sample object"
        print("disconnect_id:", {obj.group})
        pass

    def __add_obj(self, data: AddObj):
        if isinstance(data, AddObj):
            return self.__draw_board.add_obj(data)
        else:
            return -1

    def __remove_obj(self, data):
        Dictionary.remove(data.id())

    def __update_image(self, data: [Identity, ConnectorType]):
        print("update_image_blank")

    def call(self, event: Event, data):
        if event is Event.CONNECT_ID:
            return self.__connect_id(data)

        if event is Event.DISCONNECT_ID:
            return self.__disconnect_id(data)

        if event is Event.ADD_OBJ:
            return self.__add_obj(data)

        if event is Event.REMOVE_OBJ:
            return self.__remove_obj(data)

        if event is Event.UPDATE_IMG:
            return self.__update_image(data)

    def __remove_connections(self, item_id: Identity):
        pass
