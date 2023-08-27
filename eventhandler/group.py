from lines import Connection
from eventhandler import Identity, Dictionary
from object.object import Object


class Group:

    def __init__(self, identity):
        self.pool = list()
        self.__interfaces = []
        self.__identity = identity

    def add(self, first_id: Identity, second_id: Identity = None):
        if second_id is not None:
            self.gen_graphic(first_id, second_id)
        self.pool.append(Dictionary.get(first_id.obj_id()))

    def gen_graphic(self, first_id: Identity, second_id: Identity):
        first_con = Dictionary.get(first_id.obj_id())
        interface = Connection(first_id, second_id)
        self.__interfaces.append(interface)

    def __seperator(self, obj_id: Object, loop=[]):
        while self.pool.count(obj_id):
            loop.append(obj_id)
            self.pool.remove(obj_id)

        for con in Object.get_connectors():
            other_obj = self.__dict[con.linked()]
            if self.pool.count(other_obj):
                loop.append(other_obj)
                self.__seperator(other_obj, loop)

        return loop

    def separate(self, obj_id: Object):
        separated_pool = self.__seperator(obj_id)
        if not self.pool:
            self.pool = separated_pool
            return []
        else:
            return separated_pool

    def add_pools(self, other_pool):
        for identity in other_pool.pool:
            self.__dict[identity].pool = self
            self.pool.append(identity)

        del other_pool.pool
