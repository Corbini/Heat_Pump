import unittest
from eventhandler.group import Group, Dictionary, Identity


class TestDictionary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Dictionary()

    def tearDown(self):
        Dictionary.clear()

    def test_add(self):
        first_identity = Identity(1, 0)
        Dictionary.add("first", 1)
        second_identity = Identity(2, 0)
        Dictionary.add("second", 2)
        group = Group(1)

        group.add(first_identity)
        self.assertEqual(group.pool.count(Dictionary.get(1)), 1)

    def test_gen_graphic(self):
        first_identity = Identity(1, 0)
        Dictionary.add("first", 1)
        second_identity = Identity(2, 0)
        Dictionary.add("second", 2)
        group = Group(1)

        pass

    def test_seperator(self):
        pass

    def test_separate(self):
        pass

    def test_add_pools(self):
        pass


if __name__ == '__main__':
    unittest.main()
